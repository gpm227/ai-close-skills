"""Write an evidence-linked CSV and coverage report from already-inspected pages."""
import argparse
import csv
import json
import os
import tempfile
from collections import Counter
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path
from urllib.parse import urlsplit


def safe_text(text):
    if text.startswith(("\t", "\r", "\n")) or text.lstrip().startswith(("=", "+", "-", "@")):
        return "'" + text
    return text


def cell(value, kind):
    if value is None or value == "":
        return ""
    if not isinstance(value, str):
        raise ValueError("Supply published values as literal strings, or null for missing")
    if kind == "number":
        try:
            number = Decimal(value)
        except InvalidOperation as error:
            raise ValueError(f"Invalid numeric field: {value!r}") from error
        if not number.is_finite():
            raise ValueError(f"Non-finite numeric field: {value!r}")
        return str(number)
    return value


def comparison_value(value, kind):
    return Decimal(value) if value and kind == "number" else value


def extract(document):
    fields = document["fields"]
    keys = document["key"]
    metadata = {"source_url", "observed_date"}
    if (not isinstance(fields, dict) or not fields or metadata.intersection(fields)
            or any(not label.strip() or safe_text(label) != label for label in fields)
            or any(kind not in {"text", "number"} for kind in fields.values())):
        raise ValueError("Use named text/number fields distinct from the source columns")
    if not isinstance(keys, list) or not keys or len(keys) != len(set(keys)) or set(keys) - fields.keys():
        raise ValueError("Supply a unique key using one or more declared columns")
    if not isinstance(document["pages"], list):
        raise ValueError("Supply a list of discovered pages")

    pages, groups, exceptions, seen = [], {}, [], set()
    for page in document["pages"]:
        url, status = page["url"], page["status"]
        split = urlsplit(url)
        if split.scheme not in {"http", "https"} or not split.hostname or url in seen:
            raise ValueError(f"Each page needs one unique public source URL: {url!r}")
        seen.add(url)
        rows = page.get("rows", [])
        if status not in {"read", "failed", "pending", "excluded"} or not isinstance(rows, list):
            raise ValueError(f"Invalid page status or rows for {url}")
        if status != "read" and (rows or not page.get("reason")):
            raise ValueError(f"An unread page needs a reason and cannot supply rows: {url}")
        pages.append(dict(url=url, status=status, reason=page.get("reason", ""), observations=len(rows)))
        if status != "read":
            continue
        observed = date.fromisoformat(page["observed_date"]).isoformat()
        for index, row in enumerate(rows, 1):
            if set(row) - fields.keys():
                raise ValueError(f"Undeclared field on {url}, observation {index}")
            values = {name: cell(row.get(name), kind) for name, kind in fields.items()}
            source = dict(source_url=url, observed_date=observed, observation=index)
            if any(not values[name].strip() for name in keys):
                exceptions.append(dict(reason="missing key", values=values, **source))
                continue
            key = tuple(comparison_value(values[name], fields[name]) for name in keys)
            groups.setdefault(key, []).append((values, source))

    records, conflicts, duplicate_groups, text_escapes = [], [], [], []
    repeated = 0
    for observations in groups.values():
        values, source = observations[0]
        retained = values.copy()
        identity = {name: values[name] for name in keys}
        supplemental_fields = {}
        for name, kind in fields.items():
            published = {}
            for entry, ref in observations:
                if entry[name] != "":
                    published.setdefault(comparison_value(entry[name], kind), entry[name])
            if len(published) > 1:
                retained[name] = ""
                evidence = [{**ref, "value": entry[name]} for entry, ref in observations]
                conflicts.append(dict(key=identity, field=name, observations=evidence))
            elif published and retained[name] == "":
                retained[name] = next(iter(published.values()))
                supplemental_fields[name] = [ref for entry, ref in observations if entry[name] != ""]
            if kind == "text" and safe_text(retained[name]) != retained[name]:
                text_escapes.append(dict(key=identity, field=name, source_value=retained[name]))
        if len(observations) > 1:
            duplicate_groups.append(dict(key=identity, observations=[ref for entry, ref in observations],
                                         supplemental_fields=supplemental_fields))
        records.append({**retained, "source_url": source["source_url"],
                        "observed_date": source["observed_date"]})
        repeated += len(observations) - 1

    counts = Counter(page["status"] for page in pages)
    audit = dict(page_counts={status: counts[status] for status in ("read", "failed", "pending", "excluded")},
                 observations=sum(page["observations"] for page in pages), retained=len(records),
                 repeated_key_observations=repeated, unresolved_key_observations=len(exceptions),
                 missing_fields={name: sum(row[name] == "" for row in records) for name in fields},
                 pages=pages, key_exceptions=exceptions, conflicts=conflicts,
                 duplicate_groups=duplicate_groups, text_escapes=text_escapes)
    return fields, records, audit


def export(document, output):
    if output.exists() or output.is_symlink():
        raise ValueError("Choose a new output directory")
    fields, records, audit = extract(document)
    with tempfile.TemporaryDirectory(dir=output.parent) as temp:
        staged = Path(temp) / "result"
        staged.mkdir()
        with (staged / "records.csv").open("w", encoding="utf-8", newline="") as target:
            writer = csv.writer(target, quoting=csv.QUOTE_ALL)
            writer.writerow([*fields, "source_url", "observed_date"])
            for row in records:
                writer.writerow([safe_text(row[k]) if kind == "text" else row[k] for k, kind in fields.items()]
                                + [row["source_url"], row["observed_date"]])
        (staged / "coverage.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n",
                                             encoding="utf-8")
        os.rename(staged, output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("observations", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    try:
        export(json.loads(args.observations.read_text(encoding="utf-8")), args.output)
    except (OSError, ValueError, KeyError, TypeError, AttributeError, csv.Error) as exc:
        parser.exit(1, f"Cannot export: {exc}\n")
