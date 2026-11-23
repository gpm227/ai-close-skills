"""Build or verify standalone ChatGPT uploads from the skill directories."""
import argparse
import io
from pathlib import Path
from zipfile import ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "plugins/department-skills/skills"
OUTPUT = ROOT / "chatgpt"
RESOURCE_DIRS = ("agents", "assets", "examples", "references", "scripts")


def setup_note(skill):
    opening = (
        "# Install this skill in ChatGPT\n\n"
        "Open Plugins → Skills → Create → Upload from your computer and select the original ZIP. "
        "After the upload scan, start a fresh chat and try the worked practice case. "
        "[Workspace permissions and upload instructions](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)\n\n"
    )
    if (skill / "RELEASE.json").is_file():
        return opening + ("Your company owns this release. Read `company/DEPLOY.md` in the private repository "
                          "for team setup, updates and rollback. Use the included `RELEASE.json` to identify the version.\n")
    return opening + (
        "[Find this download in the catalog](https://github.com/gpm227/ai-close-skills/blob/main/CATALOG.md) · "
        "[Read the deployment guide](https://github.com/gpm227/ai-close-skills/blob/main/company/DEPLOY.md)\n"
    )


def bundle(skill):
    files = [skill / "SKILL.md"]
    if (skill / "RELEASE.json").is_file():
        files.append(skill / "RELEASE.json")
    for directory in RESOURCE_DIRS:
        for path in (skill / directory).rglob("*"):
            if any(part.startswith(".") or part == "__pycache__" for part in path.relative_to(skill).parts):
                continue
            if path.is_symlink():
                raise ValueError(f"Unexpected symbolic link: {path}")
            if path.is_file() and path.suffix != ".pyc":
                files.append(path)

    content = io.BytesIO()
    with ZipFile(content, "w") as archive:
        items = {path.relative_to(skill.parent).as_posix(): path.read_bytes() for path in files}
        items[f"{skill.name}/SETUP.md"] = setup_note(skill).encode("utf-8")
        for name, content_bytes in sorted(items.items()):
            entry = ZipInfo(name)
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, content_bytes)
    return content.getvalue()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify every archive without writing")
    args = parser.parse_args()
    skills = sorted(path.parent for path in SKILLS.glob("*/SKILL.md"))
    if not skills:
        parser.exit(1, "No skills found.\n")
    stale = {p.stem for p in OUTPUT.glob("*.zip")} - {p.name for p in skills}
    if stale:
        parser.exit(1, "Obsolete downloads: " + ", ".join(sorted(stale)) + "\n")
    if not args.check:
        OUTPUT.mkdir(exist_ok=True)
    for skill in skills:
        path = OUTPUT / (skill.name + ".zip")
        data = bundle(skill)
        if args.check:
            if not path.is_file() or path.read_bytes() != data:
                parser.exit(1, f"Rebuild {path.name} with company/package_chatgpt.py\n")
        else:
            path.write_bytes(data)
    print(f"{len(skills)} standalone skill downloads {'verified' if args.check else 'built'}")


if __name__ == "__main__":
    main()
