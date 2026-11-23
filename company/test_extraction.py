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
