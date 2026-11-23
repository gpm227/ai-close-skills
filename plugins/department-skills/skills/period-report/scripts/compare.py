"""Compare two month-to-date windows in a single-metric daily CSV."""
import argparse
import calendar
import csv
import json
from datetime import date, timedelta
from decimal import Decimal, InvalidOperation
from pathlib import Path


def compare(path, metric, cutoff):
    start = cutoff.replace(day=1)
    last = start - timedelta(days=1)
    prior_start = last.replace(day=1)
    prior_end = last.replace(day=min(cutoff.day, calendar.monthrange(last.year, last.month)[1]))
    windows = [(start, cutoff), (prior_start, prior_end)]
    values = {}
    with path.open(encoding="utf-8-sig", newline="") as source:
        rows = csv.DictReader(source)
        headers = rows.fieldnames or []
        if headers.count("date") != 1 or headers.count(metric) != 1 or metric == "date":
            raise ValueError("Expected one date column and one named metric column")
        for line, row in enumerate(rows, 2):
            day = date.fromisoformat(row["date"] or "")
            if not any(left <= day <= right for left, right in windows):
                continue
            if day in values:
                raise ValueError(f"Duplicate daily total for {day}")
            if None in row or not row[metric]:
                raise ValueError(f"Missing or misaligned metric on row {line}")
            value = Decimal(row[metric])
            if not value.is_finite():
                raise ValueError(f"Invalid total on row {line}")
            values[day] = value
    totals = []
    for left, right in windows:
        total = Decimal(0)
        for offset in range((right - left).days + 1):
            day = left + timedelta(days=offset)
            if day not in values:
                raise ValueError(f"Missing daily total for {day}")
            total += values[day]
        totals.append(total)
    current, prior = totals
    change = round((current - prior) * 100 / prior, 2) if prior else None
    return dict(current_start=start, current_end=cutoff, prior_start=prior_start,
                prior_end=prior_end, current_total=current, prior_total=prior, change_pct=change)


def render(result):
    # Decimal tokens retain precision in the JSON, including large transaction totals.
    fields = []
    for key, value in result.items():
        token = str(value) if isinstance(value, Decimal) else json.dumps(value, default=str)
        fields.append(f"{json.dumps(key)}: {token}")
    return "{" + ", ".join(fields) + "}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("daily", type=Path)
    parser.add_argument("--metric", required=True)
    parser.add_argument("--cutoff", required=True, type=date.fromisoformat)
    args = parser.parse_args()
    try:
        print(render(compare(args.daily, args.metric, args.cutoff)))
    except (OSError, ValueError, InvalidOperation, csv.Error) as exc:
        parser.exit(1, f"Cannot compare: {exc}\n")
