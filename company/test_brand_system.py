"""Check the single partner pilot from its downloadable package."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from zipfile import ZipFile
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]


class BrandPilot(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.work = Path(temp.name)
        with ZipFile(ROOT / "chatgpt/build-brand-system.zip") as archive:
            archive.extractall(self.work)
        examples = self.work / "build-brand-system/examples"
        self.data = json.loads((examples / "example.json").read_text())
        for image in examples.glob("*.png"):
            (self.work / image.name).write_bytes(image.read_bytes())

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

    def test_label_can_stand_alone_in_handoff_and_proof(self):
        card = self.data["sheet"]["cards"][0]
        card.pop("text", None)
        result = self.run_job()
        self.assertEqual(result.returncode, 0, result.stderr)
        proof = (self.work / "output/one-sheet.html").read_text()
        self.assertIn(f"<h2>{card['label']}</h2></article>", proof)
        self.assertIn(f"- {card['label']}\n", (self.work/"output/design-brief.md").read_text())

    def test_private_guide_when_only_an_internal_deck_is_usable(self):
        self.data["sheet"] = None
        self.data["voice"][1].pop("portable", None)
        self.data["sources"] = [src for src in self.data["sources"] if src["id"] == "D"]
        for rule in self.data["voice"] + self.data["visual"]:
            rule["refs"] = ["D"]
        self.data["inputs"]["website"] = {"state": "unavailable", "detail": "Site returned 403.", "refs": []}

        result = self.run_job()
        self.assertEqual(result.returncode, 0, result.stderr)
        output = self.work / "output"
        self.assertEqual({p.name for p in output.iterdir()}, {"guide.html", "voice-brief.md"})
        guide = (output / "guide.html").read_text()
        self.assertIn("Site returned 403.", guide)
        self.assertIn("Guide only.", guide)

    def test_design_brief_transfers_identity_without_private_rules(self):
        self.data["visual"].append({"rule": "Internal partner lockup is under embargo.",
                                    "status": "observed", "refs": ["D"]})
        self.data["heading_font_stack"] = "Arial, sans-serif"
        self.data["conflicts"] = [{"issue": "Timing differs in two accounts.",
                                   "state": "open", "refs": ["D", "S"],
                                   "decision": "Omit the timing claim until the owner checks it."}]

        result = self.run_job()
        self.assertEqual(result.returncode, 0, result.stderr)
        output = self.work / "output"
        handoff = (output / "design-brief.md").read_text()
        for token in [*self.data["color"].values(), self.data["font_stack"],
                      self.data["heading_font_stack"], "temporary wordmark", "Icon assignments"]:
            self.assertIn(token, handoff)
        self.assertNotIn("under embargo", handoff)
        self.assertNotIn("Timing differs", handoff)
        self.assertIn("Timing differs", (output / "guide.html").read_text())

    def test_portable_voice_brief_excludes_private_examples_and_approval_notes(self):
        self.data["decision"] = "Internal timing negotiation with Project Mast."
        self.data["voice"][1]["before"] = "Project Mast signed up last Tuesday."
        result = self.run_job()
        self.assertEqual(result.returncode, 0, result.stderr)
        output = self.work / "output"
        portable = (output / "voice-brief.md").read_text()
        self.assertNotIn("Project Mast", portable)
        partner = (output / "partner-guide.md").read_text()
        self.assertNotIn("Project Mast", partner)
        self.assertNotIn("Practice brief, deck page 2", partner)
        self.assertIn(self.data["color"]["ink"], partner)
        self.assertIn(self.data["voice"][1]["portable"]["after"], partner)
        self.assertIn("Internal brand guide", (output / "guide.html").read_text())
        self.assertIn(self.data["voice"][1]["portable"]["after"], portable)
        self.assertIn("Project Mast signed", (output / "guide.html").read_text())

    def test_no_cleared_voice_rules_is_explicit_in_both_portable_outputs(self):
        for rule in self.data["voice"]:
            rule["refs"] = ["D"]
            rule.pop("portable", None)
        result = self.run_job()
        self.assertEqual(result.returncode, 0, result.stderr)
        for name in ("voice-brief.md", "partner-guide.md"):
            text = (self.work / "output" / name).read_text()
            self.assertIn("No reusable public-source voice examples", text)
            self.assertNotIn(self.data["voice"][1]["after"], text)

    def test_unresolved_work_cannot_be_marked_approved(self):
        self.data["status"] = "owner-approved"
        self.data["conflicts"] = [{"issue": "Price differs.", "state": "open",
                                   "decision": "Hold price.", "refs": ["D", "S"]}]
        self.assertIn("Resolve open conflicts", self.run_job().stderr)
        self.data["conflicts"] = []
        self.data["sheet"]["destination"] = ""
        self.assertIn("unresolved destination", self.run_job().stderr)
        self.assertFalse((self.work / "output").exists())

    def test_input_and_conflict_evidence_must_be_consistent(self):
        self.data["inputs"]["website"]["state"] = "unavailable"
        self.assertIn("cannot supply evidence", self.run_job().stderr)
        self.data["inputs"]["website"]["state"] = "snapshot"
        self.data["conflicts"] = [{"issue": "Dates differ.", "state": "resolved",
                                   "decision": "Use the intake form.", "refs": ["S", "S"]}]
        self.assertIn("both sides", self.run_job().stderr)
        self.assertFalse((self.work / "output").exists())

    def test_action_note_survives_every_partner_handoff(self):
        note = "A coordinator replies by email with the sample."
        self.data["sheet"]["action_note"] = note
        self.data.pop("copy_limit", None)
        result = self.run_job()
        self.assertEqual(result.returncode, 0, result.stderr)
        for name in ("one-sheet.html", "design-brief.md", "partner-guide.md"):
            with self.subTest(artifact=name):
                self.assertIn(note, (self.work / "output" / name).read_text())

    def test_specimen_handoff_preserves_rejection_role_provenance_and_buyer_inference(self):
        result = self.run_job()
        self.assertEqual(result.returncode, 0, result.stderr)
        output = self.work / "output"
        device = self.data["sheet"]["device"]
        proof = (output / "one-sheet.html").read_text()
        self.assertIn('<figure><picture><source media="screen and (max-width: 40rem)"', proof)
        self.assertIn('<img src="data:image/png;base64,', proof)
        self.assertIn(device["finding"], proof)
        self.assertNotIn('<section class="cards">', proof)
        for name in ("design-brief.md", "partner-guide.md"):
            handoff = (output / name).read_text()
            for fragment in (device["meaning"], self.data["design_spec"]["substitution_test"],
                             self.data["design_spec"]["owner_rejections"][0]["instruction"],
                             "production choice", "verified", self.data["identity_basis"]["paper"]["basis"]):
                self.assertIn(fragment, handoff)

    def test_workshop_drawing_text_matches_the_counted_visible_words(self):
        source = self.work / "build-brand-system/examples/rivet-intake-plate.svg"
        root = ElementTree.parse(source).getroot()
        namespace = {"svg": "http://www.w3.org/2000/svg"}
        headings = root.findall("svg:g[@id='captions']/svg:text", namespace)
        details = root.findall("svg:g[@id='photo-directions']/svg:text", namespace)
        self.assertEqual(len(headings), 2)
        self.assertEqual(len(details), 2)
        words = " ".join(f"{title.text} {detail.text}" for title, detail in zip(headings, details))
        self.assertEqual(words, self.data["sheet"]["device"]["visible_words"])
        self.assertIn("Stage flat", words)

    def test_unqualified_legacy_role_is_labeled_unknown(self):
        del self.data["identity_basis"], self.data["design_spec"]
        self.data["layout"] = "sequence"
        del self.data["sheet"]["device"]
        result = self.run_job()
        self.assertEqual(result.returncode, 0, result.stderr)
        for name in ("design-brief.md", "partner-guide.md"):
            handoff = (self.work / "output" / name).read_text()
            self.assertIn("provenance unknown; proof setting only", handoff)
            self.assertIn("cannot establish visual distinctiveness", handoff)

    def test_sparse_input_yields_transcript_and_no_brand_palette_claim(self):
        for field in ("identity_basis", "design_spec", "layout", "color", "font_stack", "heading_font_stack"):
            self.data.pop(field, None)
        self.data["sheet"].pop("device")
        result = self.run_job()
        self.assertEqual(result.returncode, 0, result.stderr)
        handoff = (self.work / "output/design-brief.md").read_text()
        self.assertIn("Body text: #000000 — provenance unknown; proof setting only.", handoff)
        self.assertIn("visual direction as pending", handoff)

    def test_cited_role_and_buyer_visual_require_matching_evidence(self):
        self.data["identity_basis"]["paper"]["value"] = "#AA0011"
        self.assertIn("must match", self.run_job().stderr)
        self.data["identity_basis"]["paper"]["value"] = self.data["color"]["paper"]
        self.data["sheet"]["device"]["refs"] = ["D"]
        self.assertIn("lacks public clearance", self.run_job().stderr)
        self.assertFalse((self.work / "output").exists())

    def test_previous_editable_files_still_render(self):
        del self.data["inputs"], self.data["conflicts"], self.data["production"]
        result = self.run_job()
        self.assertEqual(result.returncode, 0, result.stderr)
        handoff = (self.work / "output/design-brief.md").read_text()
        self.assertIn("Confirm the intended composition", handoff)

    def test_failures_do_not_create_a_handoff(self):
        for field in ("uncleared", "missing_source", "duplicate_icons", "dense", "contrast", "cta", "echo"):
            with self.subTest(field=field):
                self.data = json.loads((self.work / "build-brand-system/examples/example.json").read_text())
                cards = self.data["sheet"]["cards"]
                if field=="uncleared": cards[0]["refs"]=["D"]
                if field=="missing_source": cards[0]["refs"]=["unseen"]
                if field=="duplicate_icons": cards[0]["icon"]=cards[1]["icon"]
                if field=="echo": cards[0]["text"]=cards[0]["label"]+"."
                if field=="dense": self.data["copy_limit"]=6
                if field=="contrast": self.data["color"]["ink"]=self.data["color"]["paper"]
                if field=="cta": self.data["sheet"]["destination"]="data:text/html,Hi"
                self.assertNotEqual(self.run_job().returncode,0)
                self.assertFalse((self.work/"output").exists())
