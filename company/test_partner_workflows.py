"""Run the packaged skills against public fixtures and boundary cases."""
import csv
import io
import json
import subprocess
import sys
import tempfile
import unittest
from datetime import date, timedelta
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]


class PartnerWorkflows(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.workspace = Path(temp.name)

    def script(self, skill, name):
        with ZipFile(ROOT / "chatgpt" / (skill + ".zip")) as archive:
            archive.extractall(self.workspace)
        return self.workspace / skill / "scripts" / name

    def test_examples_and_separate_sales_file(self):
        runner = self.script("build-target-accounts", "qualify.py")
        sample = runner.parents[1] / "examples"
        for scope in ("territory", "company"):
            eligible = self.workspace / (scope + ".csv")
            result = subprocess.run([sys.executable, runner, sample / "accounts.csv", sample / "sites.csv",
                                     "--states", "CO,AZ", "--scope", scope, "--minimum", "2",
                                     "--maximum", "3", "--eligible-file", eligible],
                                    capture_output=True, text=True, check=True)
            rows = list(csv.DictReader(io.StringIO(result.stdout)))
            self.assertEqual(len(rows), 6)
            expected = {"A": "eligible", "B": "excluded", "C": "needs evidence",
                        "D": "excluded", "E": "needs evidence", "F": "needs evidence"}
            if scope == "company":
                expected.update(B="eligible", F="eligible")
            self.assertEqual({r["account_id"]: r["decision"] for r in rows}, expected)
            with eligible.open() as source:
                self.assertEqual(list(csv.DictReader(source)), [r for r in rows if r["decision"] == "eligible"])
            self.assertIn("1 duplicate site rows", result.stderr)

    def test_uncertain_geography_and_orphans(self):
        runner = self.script("build-target-accounts", "qualify.py")
        accounts = self.workspace / "accounts.csv"
        sites = self.workspace / "sites.csv"
        accounts.write_text("account_id,name,excluded,roster_complete\n1,ABC,no,yes\n")
        sites.write_text("account_id,site_id,state\n1,1,CO\n1,2,CO\n1,3,\n")
        cmd = [sys.executable, runner, accounts, sites, "--scope", "territory",
               "--states", "CO", "--minimum", "2", "--maximum", "2"]
        run = subprocess.run(cmd, capture_output=True, text=True, check=True)
        self.assertEqual(next(csv.DictReader(io.StringIO(run.stdout)))["decision"], "needs evidence")
        for invalid in ("2,4,CO", "1,2,AZ"):
            with self.subTest(invalid=invalid):
                sites.write_text("account_id,site_id,state\n1,2,CO\n" + invalid + "\n")
                run = subprocess.run(cmd, capture_output=True, text=True)
                self.assertNotEqual(run.returncode, 0)
                self.assertEqual(run.stdout, "")

    def test_reporting_benchmarks(self):
        runner = self.script("period-report", "compare.py")
        for case in ("a", "b"):
            fixture = ROOT / "proof" / case
            output = subprocess.check_output([sys.executable, runner, fixture / "daily.csv",
                                              "--metric", "orders", "--cutoff", "2026-05-18"])
            self.assertEqual(json.loads(output), json.loads((fixture / "expected.json").read_text()))

    def test_reporting_leap_month_missing_zero_and_duplicates(self):
        runner = self.script("period-report", "compare.py")
        daily = self.workspace / "daily.csv"
        start = date(2024, 2, 1)
        days = [start + timedelta(days=i) for i in range(60)]
        records = [f"{day},{0 if day.month == 2 else 1}" for day in days]
        cmd = [sys.executable, runner, daily, "--metric", "orders", "--cutoff", "2024-03-31"]
        daily.write_text("date,orders\n" + "\n".join(records))
        output = json.loads(subprocess.check_output(cmd))
        self.assertIsNone(output["change_pct"])
        self.assertEqual((output["prior_end"], output["current_total"]), ("2024-02-29", 31))
        for invalid in (records[1:], records + records[:1]):
            daily.write_text("date,orders\n" + "\n".join(invalid))
            result = subprocess.run(cmd, capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(result.stdout)
