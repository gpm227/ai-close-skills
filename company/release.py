"""Stamp or verify the exact plugin content shipped by a company."""
import argparse
import hashlib
import json
import re
from pathlib import Path


def semver_key(version):
    """Compare SemVer releases without imposing an order on custom release labels."""
    if not isinstance(version, str):
        return None
    number = r"(0|[1-9][0-9]*)"
    labels = r"[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*"
    match = re.fullmatch(rf"{number}\.{number}\.{number}(?:-({labels}))?(?:\+{labels})?", version)
    if not match:
        return None
    major, minor, patch, prerelease = match.groups()
    identifiers = []
    for label in prerelease.split(".") if prerelease else ():
        if label.isdigit():
            if len(label) > 1 and label.startswith("0"):
                return None
            identifiers.append((0, int(label)))
        else:
            identifiers.append((1, label))
    # A final release follows every prerelease of the same core version.
    return (int(major), int(minor), int(patch), prerelease is None, tuple(identifiers))


def stamp(plugin, write=False):
    manifest = json.loads((plugin / ".claude-plugin/plugin.json").read_text())
    skills = sorted((plugin / "skills").glob("*/SKILL.md"))
    if not skills:
        raise ValueError("No skill instructions found")
    receipts = {skill.parent / "RELEASE.json" for skill in skills}
    hashes = {}
    for path in sorted(plugin.rglob("*")):
        relative = path.relative_to(plugin)
        if "__pycache__" in relative.parts or path.suffix == ".pyc":
            continue
        if path.is_symlink():
            raise ValueError(f"Unsupported symbolic link: {path}")
        if path.is_file() and path not in receipts:
            hashes[relative.as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    digest = hashlib.sha256(json.dumps(hashes, sort_keys=True).encode()).hexdigest()
    version = manifest["version"]
    precedence = semver_key(version)
    records = {}
    for skill in skills:
        receipt = skill.parent / "RELEASE.json"
        record = {"plugin": manifest["name"], "version": version,
                  "skill": skill.parent.name, "plugin_sha256": digest}
        old = json.loads(receipt.read_text()) if receipt.is_file() else None
        if old != record and not write:
            raise ValueError(f"Missing or stale release receipt: {receipt}")
        if old and old["plugin_sha256"] != digest:
            previous = semver_key(old["version"])
            if old["version"] == version or (
                previous is not None and precedence is not None and precedence <= previous
            ):
                raise ValueError("Increase the plugin version before stamping changed content")
        records[receipt] = record
    if write:
        for path, record in records.items():
            path.write_text(json.dumps(record, indent=2) + "\n")
    return {"plugin": manifest["name"], "version": manifest["version"],
            "skills": len(skills), "plugin_sha256": digest}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["stamp", "verify"])
    parser.add_argument("plugin", type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(stamp(args.plugin, args.action == "stamp"), indent=2))
    except (OSError, ValueError, KeyError) as exc:
        parser.exit(1, f"{exc}\n")
