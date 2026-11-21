"""Stamp or verify the exact plugin content shipped by a company."""
import argparse
import hashlib
import json
from pathlib import Path


def stamp(plugin, write=False):
    manifest = json.loads((plugin / ".claude-plugin/plugin.json").read_text())
    skills = sorted((plugin / "skills").glob("*/SKILL.md"))
    if not skills:
        raise ValueError("No skill instructions found")
    receipts = {skill.parent / "RELEASE.json" for skill in skills}
    hashes = {}
    for path in sorted(plugin.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"Unsupported symbolic link: {path}")
        if path.is_file() and path not in receipts:
            hashes[path.relative_to(plugin).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    digest = hashlib.sha256(json.dumps(hashes, sort_keys=True).encode()).hexdigest()
    records = {}
    for skill in skills:
        receipt = skill.parent / "RELEASE.json"
        record = {"plugin": manifest["name"], "version": manifest["version"],
                  "skill": skill.parent.name, "plugin_sha256": digest}
        old = json.loads(receipt.read_text()) if receipt.is_file() else None
        if old != record and not write:
            raise ValueError(f"Missing or stale release receipt: {receipt}")
        if old and old["version"] == record["version"] and old["plugin_sha256"] != digest:
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
