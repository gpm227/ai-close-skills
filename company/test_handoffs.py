"""Check that portable skills and shipped downloads contain no publisher promotion."""
import json
import re
import unittest
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
PUBLISHER = re.compile(rb"ai[\s_-]*close|scope an installation|utm_source=agent-skill", re.I)


class PublisherNeutralTests(unittest.TestCase):
    def test_installable_content_is_neutral(self):
        plugin = ROOT / "plugins/department-skills"
        marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        entry, = [item for item in marketplace["plugins"] if item["name"] == "department-skills"]
        self.assertIsNone(PUBLISHER.search(json.dumps(entry).encode()))
        files = list(plugin.rglob("*"))
        for file in files:
            if file.is_file() and "__pycache__" not in file.parts:
                with self.subTest(path=file.relative_to(ROOT)):
                    if file == plugin / "LICENSE":
                        self.assertIn(b"Copyright (c) 2026 AI Close contributors", file.read_bytes())
                        continue
                    self.assertIsNone(PUBLISHER.search(file.read_bytes()))

    def test_download_contents_are_neutral(self):
        for path in (ROOT / "chatgpt").glob("*.zip"):
            with ZipFile(path) as archive:
                for name in archive.namelist():
                    with self.subTest(download=path.name, entry=name):
                        content = archive.read(name)
                        if name == f"{path.stem}/LICENSE":
                            self.assertEqual(content, (ROOT / "plugins/department-skills/LICENSE").read_bytes())
                            continue
                        if Path(name).name == "SETUP.md":
                            links = re.findall(
                                rb"https://github\.com/gpm227/ai-close-skills/blob/([a-f0-9]{40})/"
                                rb"(CATALOG\.md|company/DEPLOY\.md)(?=\))", content)
                            self.assertCountEqual([page for _, page in links],
                                                  [b"CATALOG.md", b"company/DEPLOY.md"])
                            self.assertEqual(len({revision for revision, _ in links}), 1)
                            for revision, page in links:
                                source_link = b"https://github.com/gpm227/ai-close-skills/blob/" + revision + b"/" + page
                                content = content.replace(source_link, b"")
                        self.assertIsNone(PUBLISHER.search(content))
