"""Compare month-to-date windows in a daily CSV. Print JSON only after validation."""
import argparse
import csv
import json
from datetime import date, datetime, timedelta
from decimal import Decimal, DecimalException, InvalidOperation, localcontext
from fractions import Fraction
from pathlib import Path


def compare(path, metric, cutoff, unit_column=None, date_column="date", date_format="iso"):
    start = cutoff.replace(day=1)
    if start == date.min:
        raise ValueError("The date range has no representable previous month")
    last = start - timedelta(days=1)
    prior_start = last.replace(day=1)
    prior_end = last.replace(day=min(cutoff.day, last.day))
    windows = [(start, cutoff), (prior_start, prior_end)]
    values = {}
    units = set()
    with path.open(encoding="utf-8-sig", newline="") as source:
        rows = csv.DictReader(source, strict=True)
        headers = rows.fieldnames or []
        required = [date_column, metric] + ([unit_column] if unit_column is not None else [])
        if len(set(required)) != len(required) or any(headers.count(key) != 1 for key in required):
            raise ValueError("Specify distinct, unambiguous date, metric and optional unit columns")
        for row in rows:
            line = rows.line_num
            try:
                raw_date = (row[date_column] or "").strip()
                if date_format == "iso":
                    day = date.fromisoformat(raw_date)
                else:
                    day = datetime.strptime(raw_date, date_format).date()
            except ValueError as error:
                raise ValueError(f"Invalid date on line {line}") from error
            if not any(left <= day <= right for left, right in windows):
                continue
            if day in values:
                raise ValueError(f"Duplicate daily total for {day}")
            if None in row or not row[metric]:
                raise ValueError(f"Missing or misaligned metric on line {line}")
            try:
                value = Decimal(row[metric])
            except InvalidOperation as error:
                raise ValueError(f"Invalid total on line {line}") from error
            if not value.is_finite():
                raise ValueError(f"Invalid total on line {line}")
            if unit_column:
                unit = (row[unit_column] or "").strip()
                if not unit:
                    raise ValueError(f"Missing unit on line {line}")
                units.add(unit)
                if len(units) > 1:
                    raise ValueError("Covered dates contain mixed units")
            values[day] = value

    amounts = []
    for left, right in windows:
        covered = []
        for offset in range((right - left).days + 1):
            day = left + timedelta(days=offset)
            if day not in values:
                raise ValueError(f"Missing daily total for {day}")
            covered.append(values[day])
        amounts.append(covered)

    # Account for all integer and fractional places before adding up to 31 days.
    # Rational arithmetic also preserves exact ties when rounding to a hundredth.
    highest = max((value.adjusted() for value in values.values() if value), default=0)
    lowest = min(0, *(value.as_tuple().exponent for value in values.values()))
    with localcontext() as context:
        context.prec = max(28, highest - lowest + 5)
        current, prior = (sum(window, Decimal(0)) for window in amounts)
        change = None
        if prior:
            percent = (Fraction(current) - Fraction(prior)) * 100 / Fraction(prior)
            hundredths = round(percent * 100)
            change = Decimal(hundredths).scaleb(-2)
    return dict(current_start=start, current_end=cutoff, prior_start=prior_start,
                prior_end=prior_end, current_total=current, prior_total=prior, change_pct=change)


def render(result):
    # Preserve decimal tokens as JSON numbers; converting to float loses information.
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
    parser.add_argument("--unit-column", help="Require one nonempty unit across covered rows")
    parser.add_argument("--date-column", default="date", help="Exact header of the local reporting date")
    parser.add_argument("--date-format", default="iso", choices=("iso", "%m/%d/%Y", "%d/%m/%Y"),
                        help="Use the date order documented by the source export")
    args = parser.parse_args()
    try:
        print(render(compare(args.daily, args.metric, args.cutoff, args.unit_column,
                             args.date_column, args.date_format)))
    except (OSError, ValueError, DecimalException, csv.Error) as exc:
        parser.exit(1, f"Cannot compare: {exc}\n")
