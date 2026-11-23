"""Build or verify standalone ChatGPT uploads from the skill directories."""
import argparse
import io
import re
from pathlib import Path
from zipfile import ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "plugins/department-skills/skills"
OUTPUT = ROOT / "chatgpt"
RESOURCE_DIRS = ("agents", "assets", "examples", "references", "scripts")
# This edition includes the catalog, deployment guide and the reviewed downloads.
PUBLIC_EDITION = "https://github.com/gpm227/ai-close-skills/blob/4637172068a9be34d32764b05c07a5dd33c586df"


def setup_note(skill):
    instructions = (skill / "SKILL.md").read_text(encoding="utf-8")
    starter = re.search(r"(?m)^## Try it on your work\n\n[^\n]+\n\n> [^\n]+", instructions)
    if starter:
        first_run = starter.group() + "\n\n"
    else:
        # Private company skills may use their own instruction structure.
        first_run = "Open a fresh chat, give it the task and attach the material you want it to use.\n\n"
    example = next((path for path in ("examples/practice.md", "examples/brief.md")
                    if (skill / path).is_file()), None)
    if example:
        first_run += f"To try the skill with sample material, open [{example}]({example}).\n\n"
    opening = (
        "# Use this skill in ChatGPT\n\n"
        "In a workspace with Skills enabled, open **Plugins → Skills → Create → Upload from your computer**. "
        "Select the original ZIP. After the scan, confirm the skill is installed and start a fresh chat. "
        "Use the request below with your own material. You can unzip a copy to read the bundled examples.\n\n"
        "For a manual trial when Skills is unavailable, attach `SKILL.md` and the inputs or supporting files "
        "it calls for in a fresh chat. A task that uses a script needs a chat that can run code. "
        "[Workspace permissions and upload instructions](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)\n\n"
    )
    opening += first_run
    if (skill / "RELEASE.json").is_file():
        return opening + ("Your company owns this release. Read `company/DEPLOY.md` in the private repository "
                          "for team setup, updates and rollback. Use the included `RELEASE.json` to identify the version.\n")
    return opening + (
        f"[Browse the skills in this edition]({PUBLIC_EDITION}/CATALOG.md) · "
        f"[Read the deployment guide]({PUBLIC_EDITION}/company/DEPLOY.md)\n"
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
