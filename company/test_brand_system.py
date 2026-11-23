"""Check the single partner pilot from its downloadable package."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]


class BrandPilot(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.work = Path(temp.name)
        with ZipFile(ROOT / "chatgpt/build-brand-system.zip") as archive:
            archive.extractall(self.work)
        self.data = json.loads((ROOT / "examples/brand-system/example.json").read_text())

    def run_job(self):
        source = self.work / "brand.json"
        source.write_text(json.dumps(self.data))
        return subprocess.run([sys.executable,self.work / "build-brand-system/scripts/render.py",
                               source,self.work / "output"], capture_output=True, text=True)

    def test_partner_outputs(self):
        result = self.run_job()
        self.assertEqual(result.returncode,0,result.stderr)
        output = self.work / "output"
        handoff = (output / "design-brief.md").read_text()
        self.assertIn(self.data["production"]["relationship"], handoff)
        self.assertIn("visual review pending", handoff)
        self.assertNotIn("Last season 18 pieces", handoff)
        sheet = (output / "one-sheet.html").read_text()
        self.assertEqual(sheet.count('<svg aria-hidden="true"'),3)
        self.assertIn("Show us the break.",sheet)
        self.assertNotIn("turnaround figures",sheet.lower())
        self.assertIn("Practice brief, deck page 2",(output/"guide.html").read_text())
        self.assertIn("Send a photo of the break.",(output/"voice-brief.md").read_text())

    def test_failures_do_not_create_a_handoff(self):
        for field in ("uncleared", "missing_source", "duplicate_icons", "dense", "contrast", "cta"):
            with self.subTest(field=field):
                self.data = json.loads((ROOT / "examples/brand-system/example.json").read_text())
                cards = self.data["sheet"]["cards"]
                if field=="uncleared": cards[0]["refs"]=["D"]
                if field=="missing_source": cards[0]["refs"]=["unseen"]
                if field=="duplicate_icons": cards[0]["icon"]=cards[1]["icon"]
                if field=="dense": self.data["copy_limit"]=6
                if field=="contrast": self.data["color"]["ink"]=self.data["color"]["paper"]
                if field=="cta": self.data["sheet"]["destination"]="data:text/html,Hi"
                self.assertNotEqual(self.run_job().returncode,0)
                self.assertFalse((self.work/"output").exists())
