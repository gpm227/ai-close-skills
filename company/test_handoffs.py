"""Check that portable skills and shipped downloads contain no publisher promotion."""
import re
import unittest
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
PUBLISHER = re.compile(rb"ai[\s_-]*close|scope an installation|utm_source=agent-skill", re.I)


class PublisherNeutralTests(unittest.TestCase):
    def test_installable_content_is_neutral(self):
        plugin = ROOT / "plugins/department-skills"
        files = [ROOT / ".claude-plugin/marketplace.json", *plugin.rglob("*")]
        for file in files:
            if file.is_file() and "__pycache__" not in file.parts:
                with self.subTest(path=file.relative_to(ROOT)):
                    self.assertIsNone(PUBLISHER.search(file.read_bytes()))

    def test_download_contents_are_neutral(self):
        for path in (ROOT / "chatgpt").glob("*.zip"):
            with ZipFile(path) as archive:
                for name in archive.namelist():
                    with self.subTest(download=path.name, entry=name):
                        self.assertIsNone(PUBLISHER.search(archive.read(name)))
