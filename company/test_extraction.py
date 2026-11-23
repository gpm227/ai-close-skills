"""Run the exact public directory-export download on synthetic directory observations."""
import csv
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]


class PackagedExtractionTest(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.workspace = Path(temp.name)
        with ZipFile(ROOT / "chatgpt/extract-site-data.zip") as archive:
            archive.extractall(self.workspace)
        self.skill = self.workspace / "extract-site-data"
        self.example = self.skill / "examples/observations.json"
        self.output = self.workspace / "result"

    def run_export(self, observations):
        return subprocess.run(
            [sys.executable, "scripts/export_rows.py", str(observations), str(self.output)],
            cwd=self.skill, capture_output=True, text=True,
        )

    def test_published_observations(self):
        result = self.run_export(self.example)
        self.assertEqual(result.returncode, 0, result.stderr)
        with (self.output / "records.csv").open(encoding="utf-8", newline="") as source:
            rows = list(csv.DictReader(source))
        self.assertEqual([row["id"] for row in rows], ["B1", "B2", "B3"])
        self.assertEqual(rows[1], {
            "id": "B2", "name": "'=North Annex", "phone": "",
            "source_url": "https://directory.example/p1", "observed_date": "2026-06-12",
        })
        audit = json.loads((self.output / "coverage.json").read_text(encoding="utf-8"))
        self.assertEqual(audit["observations"], 4)
        self.assertEqual(audit["retained"], 3)
        self.assertEqual(audit["repeated_key_observations"], 1)
        self.assertEqual(audit["unresolved_key_observations"], 0)
        self.assertEqual(audit["page_counts"], {"read": 2, "failed": 1, "pending": 0, "excluded": 0})
        self.assertEqual(audit["missing_fields"]["phone"], 1)
        self.assertEqual(audit["text_escapes"], [
            {"key": {"id": "B2"}, "field": "name", "source_value": "=North Annex"},
        ])

    def test_merge_supplemental_fields_and_quarantine_real_disagreements(self):
        document = json.loads(self.example.read_text(encoding="utf-8"))
        # An index omits a phone published on the detail page. A second source
        # actually disagrees on the name, so only that field needs review.
        document["pages"][0]["rows"][0]["phone"] = None
        document["pages"][1]["rows"][0]["name"] = "Oak Depot"
        input_path = self.workspace / "overlap.json"
        input_path.write_text(json.dumps(document), encoding="utf-8")
        result = self.run_export(input_path)
        self.assertEqual(result.returncode, 0, result.stderr)
        with (self.output / "records.csv").open(encoding="utf-8", newline="") as source:
            branch = next(csv.DictReader(source))
        self.assertEqual(branch["phone"], "555-0101")
        self.assertEqual(branch["name"], "")
        self.assertEqual(branch["source_url"], "https://directory.example/p1")
        audit = json.loads((self.output / "coverage.json").read_text(encoding="utf-8"))
        group, = audit["duplicate_groups"]
        self.assertEqual(group["key"], {"id": "B1"})
        self.assertEqual(len(group["observations"]), 2)
        self.assertEqual(group["supplemental_fields"]["phone"], [
            {"source_url": "https://directory.example/p2", "observed_date": "2026-06-12", "observation": 1},
        ])
        conflict, = audit["conflicts"]
        self.assertEqual(conflict["field"], "name")
        self.assertEqual([item["value"] for item in conflict["observations"]], ["Oak Yard", "Oak Depot"])

    def test_decimal_spellings_agree_without_losing_text_identity(self):
        rows = [{"size": "2", "product": "01", "rate": "20.00"},
                {"size": "2.0", "product": "01", "rate": "20"},
                {"size": "2", "product": "1", "rate": "0"}]
        document = {"fields": {"size": "number", "product": "text", "rate": "number"},
                    "key": ["size", "product"],
                    "pages": [{"url": "https://prices.example/list", "status": "read",
                               "observed_date": "2026-06-12", "rows": rows}]}
        input_path = self.workspace / "rates.json"
        input_path.write_text(json.dumps(document), encoding="utf-8")
        result = self.run_export(input_path)
        self.assertEqual(result.returncode, 0, result.stderr)
        with (self.output / "records.csv").open(encoding="utf-8", newline="") as source:
            output_rows = list(csv.DictReader(source))
        self.assertEqual([(r["product"], r["rate"]) for r in output_rows], [("01", "20.00"), ("1", "0")])
        audit = json.loads((self.output / "coverage.json").read_text(encoding="utf-8"))
        self.assertEqual(audit["conflicts"], [])
        self.assertEqual(audit["repeated_key_observations"], 1)

    def test_unread_page_cannot_supply_records(self):
        document = json.loads(self.example.read_text(encoding="utf-8"))
        document["pages"][2]["rows"] = [{"id": "B4", "name": "Unobserved branch"}]
        bad = self.workspace / "invalid-observations.json"
        bad.write_text(json.dumps(document), encoding="utf-8")
        result = self.run_export(bad)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unread page", result.stderr)
        self.assertFalse(self.output.exists())


if __name__ == "__main__":
    unittest.main()
