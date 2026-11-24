"""Regression tests for decisive disqualifiers and paired CSV delivery."""
import csv
import io
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SKILL = Path(__file__).resolve().parents[1] / "plugins/department-skills/skills/build-target-accounts"


class QualificationTest(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.work = Path(temp.name)
        self.accounts = self.work / "accounts.csv"
        self.sites = self.work / "sites.csv"
        self.accounts.write_text("account_id,name,excluded,roster_complete\n01,Delta,no,unknown\n")
        self.sites.write_text("account_id,site_id,state\n01,A,CA\n01,B,CA\n")

    def qualify(self, scope, maximum, *options):
        return subprocess.run(
            [sys.executable, str(SKILL / "scripts/qualify.py"), self.accounts, self.sites,
             "--states", "CO", "--minimum", "0", "--maximum", str(maximum), "--scope", scope,
             *options],
            capture_output=True, text=True,
        )

    def test_territory_presence_and_size_must_be_simultaneously_possible(self):
        cases = [
            # Any newly discovered CO site would exceed the company-wide cap.
            ("company", 2, "excluded"),
            ("company", 3, "needs evidence"),
            # The two CA sites do not consume any of the territory-only cap.
            ("territory", 2, "needs evidence"),
            # At least one territory site is required under both scopes.
            ("territory", 0, "excluded"),
        ]
        for scope, maximum, decision in cases:
            with self.subTest(scope=scope, maximum=maximum):
                result = self.qualify(scope, maximum)
                self.assertEqual(result.returncode, 0, result.stderr)
                rows = list(csv.DictReader(io.StringIO(result.stdout)))
                self.assertEqual([(row["account_id"], row["decision"]) for row in rows],
                                 [("01", decision)])

    def test_existing_eligible_file_cannot_leave_a_partial_decision_export(self):
        ledger = self.work / "decisions.csv"
        eligible = self.work / "eligible.csv"
        eligible.write_text("previous export\n")
        result = self.qualify("company", 3, "--decisions-file", ledger, "--eligible-file", eligible)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(ledger.exists())
        self.assertEqual(eligible.read_text(), "previous export\n")

    def test_same_destination_and_input_collisions_are_rejected(self):
        output = self.work / "decisions.csv"
        original = self.accounts.read_bytes()
        for ledger, eligible in [(output, output), (self.accounts, output)]:
            with self.subTest(ledger=ledger, eligible=eligible):
                result = self.qualify("territory", 2, "--decisions-file", ledger, "--eligible-file", eligible)
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse(output.exists())
                self.assertEqual(self.accounts.read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
