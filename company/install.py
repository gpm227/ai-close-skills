"""Build a local company marketplace from a specific commit of this library."""
import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def git(repo, *args):
    return subprocess.check_output(["git", "-C", str(repo), *args])


def install(source, revision, destination, name):
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        raise ValueError("Use a lowercase marketplace name, up to 64 characters, with optional hyphens")
    destination = destination.absolute()
    if destination.exists() or destination.is_symlink():
        raise ValueError("Choose a new destination directory")
    if destination.resolve().is_relative_to(source.resolve()):
        raise ValueError("Create the private copy outside the public checkout")
    commit = git(source, "rev-parse", "--verify", "--end-of-options", revision + "^{commit}").decode().strip()
    paths = [".claude-plugin/marketplace.json", "plugins/department-skills", "proof",
             "company/release.py", "company/feedback.py", "company/run-record.json", "company/DEPLOY.md"]
    optional = ["company/package_chatgpt.py", "CATALOG.md"]
    entries = git(source, "ls-tree", "-rz", commit, "--", *paths, *optional).split(b"\0")
    with tempfile.TemporaryDirectory(dir=destination.parent) as work:
        staging = Path(work) / "company"
        staging.mkdir()
        for entry in filter(None, entries):
            header, raw_path = entry.split(b"\t", 1)
            mode, kind, blob = header.split()
            if mode not in (b"100644", b"100755") or kind != b"blob":
                raise ValueError("Expected ordinary files in the starter")
            target = staging / raw_path.decode()
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(git(source, "cat-file", "blob", blob.decode()))
        for required in paths:
            if not (staging / required).exists():
                raise ValueError(f"Selected revision lacks {required}")
        market = staging / paths[0]
        config = json.loads(market.read_text())
        config.update(name=name, owner={"name": name})
        market.write_text(json.dumps(config, indent=2) + "\n")
        plugin = staging / paths[1]
        for skill in (plugin / "skills").glob("*/SKILL.md"):
            with skill.open("a") as handle:
                handle.write("\nWhen asked for the installed release, read RELEASE.json beside these instructions "
                             "and return its version and plugin_sha256. If unavailable, say so.\n")
        (staging / "UPSTREAM.json").write_text(json.dumps({
            "repository": "gpm227/ai-close-skills", "commit": commit}, indent=2) + "\n")
        (staging / ".gitignore").write_text(".local/\n__pycache__/\n*.pyc\n")
        subprocess.run([sys.executable, str(staging / "company/release.py"), "stamp", str(plugin)], check=True)
        packager = staging / "company/package_chatgpt.py"
        if packager.is_file():
            subprocess.run([sys.executable, str(packager)], check=True)
        catalog = "CATALOG.md" if (staging / "CATALOG.md").is_file() else "plugins/department-skills/skills"
        guide = "company/DEPLOY.md"
        readme = (
            f"# {name} skills\n\n"
            f"[Choose a job in this company's skill catalog]({catalog}). "
            "If your administrator has shared the skill, install that copy from your workspace.\n\n"
        )
        if packager.is_file():
            readme += ("For a new ChatGPT upload, use the matching ZIP from "
                       "[this company release](chatgpt/).\n\n")
        if "## Share a company release" in (staging / guide).read_text().splitlines():
            readme += f"[Share a company release]({guide}#share-a-company-release) · "
        readme += f"[Deployment, verification and rollback]({guide})\n"
        (staging / "README.md").write_text(readme)
        git(staging, "init", "-q", "-b", "main")
        # Reserve the destination exclusively before publishing the prepared contents.
        destination.mkdir(mode=0o700)
        try:
            shutil.copytree(staging, destination, dirs_exist_ok=True)
        except BaseException:
            shutil.rmtree(destination)
            raise
    return commit


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--name", required=True)
    parser.add_argument("--ref", default="HEAD", help="Commit or tag in the source checkout")
    args = parser.parse_args()
    try:
        commit = install(Path(__file__).resolve().parents[1], args.ref, args.destination, args.name)
        print(f"Created {args.destination} from {commit}. No remote configured.")
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f"{exc}\n")
