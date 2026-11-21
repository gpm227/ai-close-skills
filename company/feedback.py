"""Record and evaluate finished synthetic period reports in a local pilot database."""
import argparse
import hashlib
import json
import sqlite3
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "proof"


def connect(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(path, timeout=20)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys = ON")
    db.executescript("""
      CREATE TABLE IF NOT EXISTS runs (
        id TEXT PRIMARY KEY, input_ref TEXT NOT NULL, artifact TEXT NOT NULL,
        case_id TEXT NOT NULL, release TEXT NOT NULL, benchmark TEXT NOT NULL,
        check_result TEXT, completed_at TEXT DEFAULT CURRENT_TIMESTAMP
      );
      CREATE TABLE IF NOT EXISTS signals (
        run_id TEXT REFERENCES runs(id), kind TEXT, value TEXT, evidence TEXT,
        observed_at TEXT DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(run_id, kind, value, evidence)
      );
    """)
    return db


def benchmark(case):
    digest = hashlib.sha256()
    for path in (PROOF / "check.py", PROOF / case / "expected.json"):
        digest.update(hashlib.sha256(path.read_bytes()).digest())
    return digest.hexdigest()


def capture(db, args):
    release = json.loads(args.receipt.read_text())
    if release.get("skill") != "period-report" or not all(
        isinstance(release.get(key), str) and release[key] for key in ("plugin", "version", "plugin_sha256")
    ):
        raise ValueError("Supply the release receipt for the period-report skill used in this run")
    payload = (args.input_ref, args.artifact.read_text(), args.case, json.dumps(release, sort_keys=True),
               benchmark(args.case))
    with db:
        db.execute("""INSERT INTO runs(id,input_ref,artifact,case_id,release,benchmark)
                      VALUES(?,?,?,?,?,?) ON CONFLICT(id) DO NOTHING""", (args.id, *payload))
        row = db.execute("SELECT input_ref,artifact,case_id,release,benchmark FROM runs WHERE id=?",
                         (args.id,)).fetchone()
        if tuple(row) != payload:
            raise ValueError("This run ID already records different evidence. Give revisions their own ID.")


def check(db, row):
    if row["benchmark"] != benchmark(row["case_id"]):
        raise ValueError("Restore the recorded benchmark to retry this pending check")
    with tempfile.TemporaryDirectory() as work:
        artifact = Path(work) / "artifact.json"
        artifact.write_text(row["artifact"])
        result = subprocess.run([sys.executable, str(PROOF / "check.py"), row["case_id"], str(artifact)],
                                capture_output=True, text=True)
    if result.returncode not in (0, 1):
        raise RuntimeError("Evaluator failed to run")
    verdict = json.loads(result.stdout)
    if verdict.get("verdict") != ("pass" if result.returncode == 0 else "fail"):
        raise ValueError("Evaluator returned an invalid result")
    with db:
        db.execute("UPDATE runs SET check_result=? WHERE id=? AND check_result IS NULL",
                   (json.dumps(verdict), row["id"]))
    return verdict


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=ROOT / ".local/feedback.sqlite3")
    commands = parser.add_subparsers(dest="command", required=True)
    finish = commands.add_parser("finish", help="Save a finished output, then run the checker")
    finish.add_argument("id")
    finish.add_argument("case", choices=("a", "b"))
    finish.add_argument("artifact", type=Path)
    finish.add_argument("--input-ref", required=True)
    finish.add_argument("--receipt", type=Path, required=True)
    commands.add_parser("retry", help="Evaluate any runs still pending")
    commands.add_parser("summary")
    reconcile = commands.add_parser("reconcile", help="Compare an independent list of completed run IDs")
    reconcile.add_argument("inventory", type=Path, help="One unique completed output ID per line")
    vote = commands.add_parser("vote")
    vote.add_argument("id")
    vote.add_argument("value", choices=("worked", "didnt-work"))
    vote.add_argument("--reason", default="")
    outcome = commands.add_parser("outcome")
    outcome.add_argument("id")
    outcome.add_argument("value")
    outcome.add_argument("--evidence", required=True)
    args = parser.parse_args()
    db = connect(args.db)
    try:
        if args.command == "finish":
            capture(db, args)
            row = db.execute("SELECT * FROM runs WHERE id=?", (args.id,)).fetchone()
            result = json.loads(row["check_result"]) if row["check_result"] else check(db, row)
            print(json.dumps(result))
            return int(result["verdict"] == "fail")
        if args.command == "retry":
            pending = db.execute("SELECT * FROM runs WHERE check_result IS NULL").fetchall()
            errors = 0
            for row in pending:
                try:
                    print(json.dumps({"id": row["id"], **check(db, row)}))
                except (OSError, RuntimeError, ValueError) as exc:
                    print(f"{row['id']}: {exc}", file=sys.stderr)
                    errors += 1
            return int(bool(errors))
        if args.command == "reconcile":
            ids = [line.strip() for line in args.inventory.read_text().splitlines() if line.strip()]
            if len(ids) != len(set(ids)):
                raise ValueError("The completed-output inventory contains duplicate IDs")
            expected = set(ids)
            observed = {r["id"]: r["check_result"] for r in db.execute("SELECT id,check_result FROM runs")}
            report = {"completed": len(expected), "checked": sum(bool(observed.get(i)) for i in expected),
                      "missing_capture": sorted(expected - observed.keys()),
                      "pending_check": sorted(i for i in expected & observed.keys() if not observed[i]),
                      "outside_inventory": sorted(observed.keys() - expected)}
            print(json.dumps(report, indent=2))
            return int(any(report[k] for k in ("missing_capture", "pending_check", "outside_inventory")))
        if args.command == "summary":
            rows = db.execute("SELECT check_result FROM runs").fetchall()
            counts = {"recorded_outputs": len(rows), "checked": 0, "passed": 0, "failed": 0, "pending": 0}
            for row in rows:
                if row[0] is None:
                    counts["pending"] += 1
                else:
                    counts["checked"] += 1
                    counts["passed" if json.loads(row[0])["verdict"] == "pass" else "failed"] += 1
            for kind in ("vote", "outcome"):
                counts["runs_with_" + kind] = db.execute(
                    "SELECT COUNT(DISTINCT run_id) FROM signals WHERE kind=?", (kind,)).fetchone()[0]
            print(json.dumps(counts, indent=2))
        else:
            evidence = args.reason if args.command == "vote" else args.evidence
            if args.command == "vote" and args.value == "didnt-work" and not evidence.strip():
                raise ValueError("Include the reason the output did not work")
            if not db.execute("SELECT 1 FROM runs WHERE id=?", (args.id,)).fetchone():
                raise ValueError("Unknown run ID")
            with db:
                db.execute("""INSERT INTO signals(run_id,kind,value,evidence) VALUES(?,?,?,?)
                              ON CONFLICT DO NOTHING""", (args.id, args.command, args.value, evidence))
        return 0
    finally:
        db.close()


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError, ValueError, sqlite3.Error) as error:
        raise SystemExit(str(error))
