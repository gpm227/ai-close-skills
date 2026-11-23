"""Exercise release identity and uploads on a disposable plugin."""
import json
import py_compile
import tempfile
import unittest
from pathlib import Path

from package_chatgpt import bundle
from release import stamp


class ReleaseTest(unittest.TestCase):
    def setUp(self):
        workspace = tempfile.TemporaryDirectory()
        self.addCleanup(workspace.cleanup)
        self.plugin = Path(workspace.name) / "plugin"
        self.manifest = self.plugin / ".claude-plugin/plugin.json"
        self.manifest.parent.mkdir(parents=True)
        self.set_version("0.8.0")
        self.skill = self.plugin / "skills/report"
        self.script = self.skill / "scripts/report.py"
        self.script.parent.mkdir(parents=True)
        self.script.write_text("total = 3\n")
        (self.skill / "SKILL.md").write_text("# Use the report\n")
        self.receipt = self.skill / "RELEASE.json"

    def set_version(self, version):
        self.manifest.write_text(json.dumps({"name": "demo", "version": version}))

    def test_caches_leave_public_and_company_releases_unchanged(self):
        public_zip = bundle(self.skill)
        cached = Path(py_compile.compile(str(self.script), doraise=True))
        loose = self.script.with_suffix(".pyc")
        loose.write_bytes(cached.read_bytes())
        self.assertEqual(bundle(self.skill), public_zip)

        stamped = stamp(self.plugin, write=True)
        company_zip = bundle(self.skill)
        self.assertNotEqual(company_zip, public_zip)
        cached.unlink()
        loose.unlink()
        self.assertEqual(stamp(self.plugin), stamped)
        self.assertEqual(bundle(self.skill), company_zip)

        self.script.write_text("total = 4\n")
        with self.assertRaisesRegex(ValueError, "stale release receipt"):
            stamp(self.plugin)
        with self.assertRaisesRegex(ValueError, "Increase"):
            stamp(self.plugin, write=True)

    def test_semantic_versions_must_advance_before_restamping(self):
        versions = ["0.8.0", "0.9.0-beta.2", "0.9.0-beta.11", "0.9.0-rc.1", "0.9.0"]
        for version in versions:
            self.set_version(version)
            self.assertEqual(stamp(self.plugin, write=True)["version"], version)
        expected_receipt = self.receipt.read_bytes()
        for version in ["0.8.9", "0.9.0-rc.2", "0.9.0+new-build"]:
            with self.subTest(version=version):
                self.set_version(version)
                with self.assertRaisesRegex(ValueError, "Increase"):
                    stamp(self.plugin, write=True)
                self.assertEqual(self.receipt.read_bytes(), expected_receipt)

    def test_custom_plugin_versions_remain_usable(self):
        for label in ["april-pilot", "may-pilot"]:
            self.set_version(label)
            self.assertEqual(stamp(self.plugin, write=True)["version"], label)
        self.script.write_text("total = 7\n")
        with self.assertRaisesRegex(ValueError, "Increase"):
            stamp(self.plugin, write=True)
