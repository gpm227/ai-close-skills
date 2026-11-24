"""Exercise the company deployment and feedback path using synthetic data."""
import importlib.util
import json
import re
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.parse import urlsplit
from zipfile import ZipFile

SOURCE = Path(__file__).resolve().parents[1]


class DeploymentTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.company = Path(self.temp.name) / "company"
        self.install = [sys.executable, str(SOURCE / "company/install.py"),
                        str(self.company), "--name", "sample-company"]
        subprocess.run(self.install, check=True, capture_output=True)
        self.plugin = self.company / "plugins/department-skills"
        self.receipt = self.plugin / "skills/period-report/RELEASE.json"
        self.expected = self.company / "proof/a/expected.json"

    def run_command(self, *args, status=0):
        result = subprocess.run(args, cwd=self.company, capture_output=True, text=True)
        self.assertEqual(result.returncode, status, result.stdout + result.stderr)
        return result.stdout

    def feedback(self, *args, status=0):
        return self.run_command(sys.executable, "company/feedback.py", *args, status=status)

    def finish(self, run_id, artifact, status=0):
        return self.feedback("finish", run_id, "a", str(artifact), "--input-ref", "case-a",
                             "--receipt", str(self.receipt), status=status)

    def test_install_and_replay(self):
        market = json.loads((self.company / ".claude-plugin/marketplace.json").read_text())
        self.assertEqual(market["name"], "sample-company")
        self.assertEqual(len(market["plugins"]), 1)
        self.assertEqual(market["plugins"][0]["source"], "./plugins/department-skills")
        expected_sha = subprocess.check_output(["git", "-C", SOURCE, "rev-parse", "HEAD"], text=True).strip()
        self.assertEqual(json.loads((self.company / "UPSTREAM.json").read_text())["commit"], expected_sha)
        self.assertEqual(self.run_command("git", "remote").strip(), "")
        published = len(list(Path(SOURCE, "plugins/department-skills/skills").glob("*/SKILL.md")))
        self.assertEqual(len(list(self.plugin.glob("skills/*/RELEASE.json"))), published)
        archives = sorted((self.company / "chatgpt").glob("*.zip"))
        self.assertEqual(len(archives), published)
        for archive in archives:
            with self.subTest(skill=archive.stem), ZipFile(archive) as installed:
                base = self.plugin / "skills" / archive.stem
                for rel in ("RELEASE.json", "SKILL.md"):
                    self.assertEqual(installed.read(f"{archive.stem}/{rel}"), (base / rel).read_bytes())
        self.run_command(sys.executable, "company/package_chatgpt.py", "--check")
        self.run_command(*self.install, status=1)
        self.run_command(sys.executable, "company/release.py", "verify", str(self.plugin))

    def test_company_readme_and_catalog_lead_to_installed_files(self):
        readme = self.company / "README.md"
        catalog = self.company / "CATALOG.md"
        guide = self.company / "company/DEPLOY.md"
        self.assertIn("](CATALOG.md)", readme.read_text())
        self.assertIn("](chatgpt/)", readme.read_text())
        self.assertNotEqual(readme.read_bytes(), guide.read_bytes())
        if "## Share a company release" in guide.read_text().splitlines():
            self.assertIn("](company/DEPLOY.md#share-a-company-release)", readme.read_text())
        downloads = re.findall(r"\]\(chatgpt/([\w-]+)\.zip\?raw=true\)", catalog.read_text())
        self.assertEqual(sorted(downloads), sorted(p.stem for p in (self.company / "chatgpt").glob("*.zip")))
        for source in (readme, catalog, guide, *(self.company / "proof").rglob("*.md")):
            for target in re.findall(r"\]\(([^ )]+)\)", source.read_text()):
                link = urlsplit(target)
                if not link.scheme and link.path:
                    with self.subTest(source=source.relative_to(self.company), target=target):
                        self.assertTrue((source.parent / link.path).exists())

    def test_change_and_rollback(self):
        skill = self.receipt.with_name("SKILL.md")
        original = skill.read_bytes()
        manifest = self.plugin / ".claude-plugin/plugin.json"
        original_version = json.loads(manifest.read_text())["version"]
        release = [sys.executable, "company/release.py"]
        skill.write_bytes(original + b"\nTemporary business rule.\n")
        self.run_command(*release, "verify", str(self.plugin), status=1)
        self.run_command(*release, "stamp", str(self.plugin), status=1)
        major, minor, patch_num = map(int, original_version.split("."))
        for offset in (1, 2):
            if offset == 2:
                skill.write_bytes(original)
            version = f"{major}.{minor}.{patch_num + offset}"
            values = json.loads(manifest.read_text())
            values["version"] = version
            manifest.write_text(json.dumps(values))
            self.run_command(*release, "stamp", str(self.plugin))
            result = self.run_command(*release, "verify", str(self.plugin))
            self.assertEqual(json.loads(result)["version"], version)
        self.assertEqual(skill.read_bytes(), original)

    def test_feedback_is_independent_and_idempotent(self):
        self.finish("report-a", self.expected)
        self.finish("report-a", self.expected)
        wrong = self.company / "wrong.json"
        values = json.loads(self.expected.read_text())
        values["prior_end"] = "2026-04-30"
        wrong.write_text(json.dumps(values))
        self.finish("report-a", wrong, status=1)
        self.assertEqual(json.loads(self.finish("report-bad", wrong, status=1))["evidence"][0]["field"],
                         "prior_end")
        for _ in range(2):
            self.feedback("vote", "report-a", "didnt-work", "--reason", "Context missing")
            self.feedback("outcome", "report-a", "used", "--evidence", "record-1")
        counts = json.loads(self.feedback("summary"))
        self.assertEqual(counts, {"recorded_outputs": 2, "checked": 2, "passed": 1, "failed": 1,
                                  "pending": 0, "runs_with_vote": 1, "runs_with_outcome": 1})
        db = sqlite3.connect(self.company / ".local/feedback.sqlite3")
        try:
            self.assertEqual(db.execute("SELECT count(*) FROM signals").fetchone()[0], 2)
        finally:
            db.close()
        inventory = self.company / "inventory.txt"
        inventory.write_text("report-a\nreport-bad\nmissing\n")
        report = json.loads(self.feedback("reconcile", str(inventory), status=1))
        self.assertEqual(report["missing_capture"], ["missing"])
        self.assertEqual(report["checked"], 2)

    def test_report_rejects_extra_fields(self):
        artifact = self.company / "extra.json"
        values = json.loads(self.expected.read_text())
        values["headline"] = "Orders fell 40%."
        artifact.write_text(json.dumps(values))
        result = self.run_command(sys.executable, "proof/check.py", "a", artifact, status=1)
        self.assertEqual(json.loads(result)["evidence"], [{"field": "headline", "error": "Unexpected field"}])

    def test_capture_survives_checker_interruption(self):
        spec = importlib.util.spec_from_file_location("installed_feedback", self.company / "company/feedback.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        argv = ["feedback", "finish", "interrupted", "a", str(self.expected), "--input-ref", "case-a",
                "--receipt", str(self.receipt)]
        with patch.object(sys, "argv", argv), patch.object(module, "check", side_effect=RuntimeError):
            with self.assertRaises(RuntimeError):
                module.main()
        self.assertEqual(json.loads(self.feedback("summary"))["pending"], 1)
        self.feedback("retry")
        self.assertEqual(json.loads(self.feedback("summary"))["passed"], 1)


if __name__ == "__main__":
    unittest.main()
