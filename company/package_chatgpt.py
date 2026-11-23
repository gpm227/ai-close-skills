"""Build deterministic, standalone uploads from the same skill sources as the team plugin."""
import argparse
import io
from pathlib import Path
from zipfile import ZIP_STORED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "plugins/department-skills/skills"
OUTPUT = ROOT / "chatgpt"
EXTERNAL_HANDOFF = "To send the finished result along with the request, follow `../../TEAM.md`."
LOCAL_HANDOFF = ("If the user wants to share the finished work, provide the link and offer a "
                 "Markdown file they can choose on the review page. The link carries only the skill "
                 "name and campaign tags. Never transfer their work automatically.")


def bundle(skill):
    files = [skill / "SKILL.md"]
    if (skill / "RELEASE.json").is_file():
        files.append(skill / "RELEASE.json")
    for subdir in ("agents", "scripts", "references", "assets"):
        files.extend(path for path in (skill / subdir).rglob("*")
                     if path.is_file() and "__pycache__" not in path.parts
                     and not path.name.startswith(".") and path.suffix != ".pyc")
    out = io.BytesIO()
    with ZipFile(out, "w") as archive:
        for path in sorted(files):
            relative = path.relative_to(skill.parent)
            data = path.read_bytes()
            if path.name == "SKILL.md":
                if EXTERNAL_HANDOFF.encode() not in data:
                    raise ValueError(f"Review standalone handoff in {relative}")
                data = data.replace(EXTERNAL_HANDOFF.encode(), LOCAL_HANDOFF.encode())
            entry = ZipInfo(relative.as_posix())
            entry.compress_type = ZIP_STORED
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, data)
    return out.getvalue()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = {OUTPUT / (p.parent.name + ".zip"): bundle(p.parent) for p in sorted(SKILLS.glob("*/SKILL.md"))}
    stale = set(OUTPUT.glob("*.zip")) - expected.keys()
    if stale:
        parser.exit(1, "Remove obsolete downloads: " + ", ".join(p.name for p in sorted(stale)) + "\n")
    for path, data in expected.items():
        if args.check:
            if not path.exists() or path.read_bytes() != data:
                parser.exit(1, f"Rebuild {path.name} with company/package_chatgpt.py\n")
        else:
            OUTPUT.mkdir(exist_ok=True)
            path.write_bytes(data)
    print(f"{len(expected)} standalone skill bundles {'verified' if args.check else 'built'}")


if __name__ == "__main__":
    main()
