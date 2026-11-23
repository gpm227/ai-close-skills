"""Produce the standalone ChatGPT upload for the partner pilot."""
import argparse
import io
from pathlib import Path
from zipfile import ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "plugins/department-skills/skills/build-brand-system"
ZIP = ROOT / "chatgpt/build-brand-system.zip"


def build():
    content = io.BytesIO()
    with ZipFile(content, "w") as archive:
        files = {name: SKILL / name for name in (
            "SKILL.md", "agents/openai.yaml", "references/format.md", "scripts/render.py",
            "examples/brief.md", "examples/example.json")}
        for name, path in files.items():
            entry = ZipInfo(f"{SKILL.name}/{name}")
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, path.read_bytes())
    return content.getvalue()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = build()
    if args.check:
        if not ZIP.is_file() or data != ZIP.read_bytes():
            parser.exit(1, "Rebuild the ChatGPT download.\n")
    else:
        ZIP.parent.mkdir(exist_ok=True)
        ZIP.write_bytes(data)
