"""Evaluate the JSON portion of a report against a frozen benchmark."""
import argparse
import json
import math
from pathlib import Path


def evaluate(expected, actual):
    failures = []
    for field, target in expected.items():
        observed = actual.get(field)
        if type(target) in (int, float):
            matches = type(observed) in (int, float) and math.isclose(
                observed, target, rel_tol=0, abs_tol=1e-9
            )
        else:
            matches = observed == target
        if not matches:
            failures.append({"field": field, "expected": target, "observed": observed})
    return failures


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case", choices=["a", "b"])
    parser.add_argument("artifact", type=Path)
    args = parser.parse_args()
    benchmark = Path(__file__).parent / args.case / "expected.json"
    expected = json.loads(benchmark.read_text())
    try:
        actual = json.loads(args.artifact.read_text())
        if not isinstance(actual, dict):
            raise ValueError("Report must be a JSON object")
        failures = evaluate(expected, actual)
    except (OSError, ValueError) as error:
        failures = [{"error": str(error)}]
    print(json.dumps({"case": args.case, "benchmark": "0.1.0",
                      "verdict": "fail" if failures else "pass",
                      "evidence": failures}, indent=2))
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
