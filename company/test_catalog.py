"""Ensure the public entry points and standalone packages expose the same jobs and resources."""
import re
import unittest
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "plugins/department-skills/skills"


class CatalogTest(unittest.TestCase):
    def test_catalog_matches_bundles_and_sources(self):
        catalog = (ROOT / "CATALOG.md").read_text()
        listed = re.findall(r"\]\(plugins/department-skills/skills/([\w-]+)/SKILL\.md\)", catalog)
        downloads = re.findall(r"\]\(chatgpt/([\w-]+)\.zip\?raw=true\)", catalog)
        sources = sorted(path.parent.name for path in SKILLS.glob("*/SKILL.md"))
        self.assertEqual(sorted(listed), sources)
        self.assertEqual(sorted(downloads), sources)

    def test_individual_downloads_include_the_practice_case(self):
        for path in SKILLS.glob("*/SKILL.md"):
            name = path.parent.name
            with self.subTest(skill=name), ZipFile(ROOT / "chatgpt" / (name + ".zip")) as archive:
                instructions = archive.read(name + "/SKILL.md").decode()
                self.assertEqual(instructions.encode(), path.read_bytes())
                self.assertRegex(instructions, rf"(?m)^name: {re.escape(name)}$")
                example = "examples/brief.md" if name == "build-brand-system" else "examples/practice.md"
                self.assertIn(example, instructions)
                self.assertEqual(archive.read(f"{name}/{example}"), (path.parent / example).read_bytes())
                for item in archive.namelist():
                    relative = Path(item).relative_to(name)
                    if relative.as_posix() == "SETUP.md":
                        self.assertIn(b"company/DEPLOY.md", archive.read(item))
                    else:
                        self.assertEqual(archive.read(item), (path.parent / relative).read_bytes())
