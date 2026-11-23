"""Qualify accounts from an account register and distinct site records."""
import argparse
import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path


def read_rows(path, required):
    with path.open(encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        if not reader.fieldnames or len(set(reader.fieldnames)) != len(reader.fieldnames) or not required.issubset(reader.fieldnames):
            raise ValueError(f"{path.name}: expected unique headers including {sorted(required)}")
        for line, row in enumerate(reader, 2):
            if None in row or None in row.values() or not row["account_id"].strip():
                raise ValueError(f"{path.name} row {line}: incomplete or misaligned record")
            yield line, {key: value.strip() for key, value in row.items()}


def run(args):
    territory = {state.strip().upper() for state in args.states.split(",")}
    if "" in territory or not 0 <= args.minimum <= args.maximum:
        raise ValueError("Provide territory codes and a valid inclusive size range")
    accounts = {}
    for line, row in read_rows(args.accounts, {"account_id", "name", "excluded", "roster_complete"}):
        key = row["account_id"]
        if key in accounts:
            raise ValueError(f"Resolve duplicate account ID {key} at row {line}")
        for field in ("excluded", "roster_complete"):
            if row[field] not in {"yes", "no", "unknown"}:
                raise ValueError(f"Use yes/no/unknown for {field} at row {line}")
        accounts[key] = (line, row)

    sites = defaultdict(dict)
    refs = defaultdict(list)
    repeats = 0
    for line, row in read_rows(args.sites, {"account_id", "site_id", "state"}):
        key, site, state = row["account_id"], row["site_id"], row["state"].upper()
        if key not in accounts or not site:
            raise ValueError(f"{args.sites.name} row {line}: unresolved account or site ID")
        if site in sites[key]:
            if sites[key][site] != state:
                raise ValueError(f"{args.sites.name} row {line}: conflicting states for {key}/{site}")
            repeats += 1
        sites[key][site] = state
        refs[key].append(str(line))

    results = []
    for key, (line, account) in accounts.items():
        states = sites[key].values()
        local = sum(state in territory for state in states)
        observed = local if args.scope == "territory" else len(states)
        complete = account["roster_complete"] == "yes"
        unknown_states = sum(not state for state in states)
        upper = observed + (unknown_states if args.scope == "territory" else 0)
        verdict = "excluded"
        if account["excluded"] == "yes":
            reason = "Confirmed exclusion"
        elif observed > args.maximum:
            reason = "Verified sites already exceed maximum"
        elif complete and upper < args.minimum:
            reason = "Complete roster below minimum"
        elif complete and local == 0 and not unknown_states:
            reason = "No site in territory"
        elif account["excluded"] == "unknown":
            verdict, reason = "needs evidence", "Verify suppression against the approved list"
        elif not complete:
            verdict, reason = "needs evidence", "Obtain complete site roster to establish upper bound"
        elif local == 0 or observed < args.minimum or upper > args.maximum:
            verdict, reason = "needs evidence", "Resolve missing site geography"
        else:
            verdict, reason = "eligible", "Verified territory presence and size within range"
        evidence = f"{args.accounts.name} row {line}"
        if refs[key]:
            evidence += f"; {args.sites.name} rows " + ",".join(refs[key])
        results.append([key, account["name"], len(states), local, unknown_states, account["roster_complete"],
                        verdict, reason, evidence])
    header = ["account_id", "name", "observed_sites", "verified_territory_sites",
              "missing_state", "roster_complete", "decision", "reason", "evidence"]
    if args.eligible_file:
        if args.eligible_file.resolve() in {args.accounts.resolve(), args.sites.resolve()}:
            raise ValueError("Choose a new eligible file, distinct from the input files")
        with args.eligible_file.open("x", encoding="utf-8", newline="") as target:
            eligible = csv.writer(target)
            eligible.writerow(header)
            eligible.writerows(row for row in results if row[6] == "eligible")
    writer = csv.writer(sys.stdout)
    writer.writerow(header)
    writer.writerows(results)
    counts = Counter(row[6] for row in results)
    print(f"{len(results)} accounts; {repeats} duplicate site rows; {dict(counts)}", file=sys.stderr)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("accounts", type=Path)
    parser.add_argument("sites", type=Path)
    parser.add_argument("--states", required=True, help="Comma-separated in-service state codes")
    parser.add_argument("--scope", choices=["territory", "company"], required=True)
    parser.add_argument("--minimum", type=int, required=True)
    parser.add_argument("--maximum", type=int, required=True)
    parser.add_argument("--eligible-file", type=Path, help="Write eligible accounts to a new CSV")
    try:
        run(parser.parse_args())
    except (ValueError, OSError, csv.Error) as error:
        parser.exit(1, f"{error}\n")
