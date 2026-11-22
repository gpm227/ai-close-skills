"""Keep every published skill usable on its own and linked to its own review."""
import re
import unittest
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

SKILLS = Path(__file__).resolve().parents[1] / 'plugins/department-skills/skills'

class SkillHandoffTests(unittest.TestCase):
    def test_every_skill_has_a_contextual_optional_handoff(self):
        for path in sorted(SKILLS.glob('*/SKILL.md')):
            with self.subTest(skill=path.parent.name):
                instructions = path.read_text()
                task, separator, handoff = instructions.partition('### Optional team implementation')
                self.assertTrue(separator)
                self.assertGreater(len(task.strip()), 150)
                links = re.findall(r'https://aiclosehq\.com/talk\?[^)\s]+', handoff)
                self.assertEqual(len(links), 1)
                query = parse_qs(urlsplit(links[0]).query)
                self.assertEqual(query['skill'], [path.parent.name])
                self.assertEqual(query['intent'], ['custom-installation'])
                self.assertEqual(query['utm_source'], ['agent-skill'])
                for condition in ('unrelated','failed output','free-output-only','declined offer'):
                    self.assertIn(condition, handoff)
