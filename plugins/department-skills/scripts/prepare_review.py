"""Prepare an offline, user-authorized handoff. Creating the file makes no network request."""
import argparse
import html
from pathlib import Path
import uuid

SKILLS = Path(__file__).resolve().parents[1] / "skills"
DESTINATION = "https://aiclosehq.com/talk/import-result"


def prepare(slug, source, destination):
    if not (SKILLS / slug / "SKILL.md").is_file() or slug not in {p.name for p in SKILLS.iterdir()}:
        raise ValueError("Choose a published skill")
    raw = source.read_bytes()
    if len(raw) > 12288:
        raise ValueError("Use manual import for results larger than 12 KB")
    text = raw.decode("utf-8")
    if not text.strip() or "\x00" in text:
        raise ValueError("Choose a non-empty UTF-8 text file")
    import base64
    encoded = base64.b64encode(raw).decode("ascii")
    revision = str(uuid.uuid4())
    document = f"""<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Review this result · AI Close</title>
<style>body{{max-width:46rem;margin:5vh auto;padding:1rem;font:17px/1.5 system-ui;background:#101415;color:#ecf1ef}}pre{{white-space:pre-wrap;overflow-wrap:anywhere;background:#202627;padding:1rem}}button{{padding:.7rem 1rem;font:inherit}}</style>
<h1>Review this result</h1><p>This private file contains your finished work. Continuing sends the displayed result to AI Close for this review. The destination keeps a copy in your browser tab. You choose separately whether to submit a meeting request.</p>
<pre>{html.escape(text)}</pre><form method="post" action="{DESTINATION}">
<input type="hidden" name="skill" value="{html.escape(slug)}"><input type="hidden" name="revision" value="{revision}"><input type="hidden" name="artifact" value="{encoded}"><button>Send this result and open the review</button></form></html>"""
    with destination.open("x", encoding="utf-8") as out:
        out.write(document)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill")
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    prepare(args.skill, args.source, args.destination)
