"""Check the public marketing index, the two install targets, and their links."""
import json
import re
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class MarketingLibraryTests(unittest.TestCase):
    def test_index_points_to_every_shipped_marketing_skill(self):
        text = (ROOT / "MARKETING-ROADMAP.md").read_text().split("## Bridges to the department library")[0]
        jobs = {}
        for line in text.splitlines():
            if not line.startswith("| ") or line.startswith(("| Skill |", "| ---")):
                continue
            label, job, status = (cell.strip() for cell in line.strip("|").split("|"))
            self.assertTrue(job)
            self.assertIn(status, ("ready", "Next", "Mapped"))
            if status == "ready":
                link = re.fullmatch(r"\[([a-z0-9-]+)\]\(skills/\1/SKILL\.md\)", label)
                self.assertIsNotNone(link, label)
                name = link.group(1)
            else:
                self.assertRegex(label, r"^[a-z0-9-]+$")
                name = label
            self.assertNotIn(name, jobs)
            jobs[name] = status

        shipped = {p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")}
        self.assertEqual({key for key, status in jobs.items() if status == "ready"}, shipped)
        self.assertIn(f"{len(jobs)} marketing jobs", text)

    def test_library_directory_covers_each_published_job_once(self):
        readme = (ROOT / "README.md").read_text()
        index = (ROOT / "SKILLS.md").read_text()
        areas = ["Sales", "Marketing", "Operations", "Reporting", "Analytics"]
        self.assertEqual(re.findall(r"^## (.+)$", index, re.M), areas)
        for area in areas:
            self.assertIn(f"## {area}\n", readme)
            self.assertIn(f"(SKILLS.md#{area.lower()})", readme)
            section = index.split(f"## {area}\n", 1)[1].split("\n## ", 1)[0]
            self.assertRegex(section, r"\| \[.+?\]\(.+?/SKILL\.md\)")
        listed = re.findall(r"^\| \[.+?\]\(([^)]+/SKILL\.md)\)", index, re.M)
        sources = [p.relative_to(ROOT).as_posix() for group in ("skills", "plugins/department-skills/skills")
                   for p in (ROOT / group).glob("*/SKILL.md")]
        self.assertCountEqual(listed, sources)
        self.assertIn(f"Browse all {len(sources)} skills", readme)

    def test_marketplace_preserves_both_install_targets(self):
        market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        self.assertEqual(market["name"], "department-workflows")
        entries = {entry["name"]: entry["source"] for entry in market["plugins"]}
        self.assertEqual(len(entries), len(market["plugins"]))
        for name, location in {"department-skills": "./plugins/department-skills", "aiclose-skills": "./"}.items():
            self.assertEqual(entries[name], location)
            plugin = ROOT / location
            manifest = json.loads((plugin / ".claude-plugin/plugin.json").read_text())
            self.assertEqual(manifest["name"], name)
            self.assertTrue(any((plugin / "skills").glob("*/SKILL.md")))

    def test_marketing_skill_contract_and_links(self):
        subprocess.run(["bash", "tools/check.sh"], cwd=ROOT, check=True, capture_output=True)
