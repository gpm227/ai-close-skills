"""Produce the standalone ChatGPT upload for the partner pilot."""
import argparse
from pathlib import Path
from package_chatgpt import bundle

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "plugins/department-skills/skills/build-brand-system"
ZIP = ROOT / "chatgpt/build-brand-system.zip"


def build():
    return bundle(SKILL)


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
