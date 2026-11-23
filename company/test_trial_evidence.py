"""Keep recorded artifacts tied to the exact task receipts that cite them."""
import hashlib
import json
from pathlib import Path
import unittest
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]


class TrialEvidenceTest(unittest.TestCase):
    def test_catalog_evidence_matches_recorded_artifacts(self):
        proof = ROOT / "proof/quality"
        jobs = {p.parent.name for p in (ROOT / "plugins/department-skills/skills").glob("*/SKILL.md")}
        cases = jobs - {"build-brand-system"}
        for filename in ("requests.json", "acceptance.json"):
            self.assertEqual(set(json.loads((proof / filename).read_text())), cases)
        results = json.loads((proof / "results.json").read_text())
        self.assertEqual(sorted(r["skill"] for r in results), sorted(cases))
        with ZipFile(proof / "worked-trials.zip") as outputs:
            for record in results:
                with self.subTest(skill=record["skill"]):
                    actual = outputs.read(record["output_file"])
                    self.assertEqual(hashlib.sha256(actual).hexdigest(), record["output_sha256"])
                    self.assertIn(record["output_evidence"], actual.decode())
