"""Compare ordered StateTree scenario markers captured from Unreal logs."""

import argparse
import difflib
import json
from collections import defaultdict
from pathlib import Path


PREFIX = "STREG "
FIELDS = ("scenario", "state", "event", "outcome")


def read_markers(path):
    scenarios = defaultdict(list)
    for number, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        if PREFIX not in line:
            continue
        try:
            marker = json.loads(line.split(PREFIX, 1)[1])
            if not isinstance(marker, dict) or any(not isinstance(marker.get(field), str) or not marker[field] for field in FIELDS):
                raise ValueError("scenario, state, event and outcome must be nonempty strings")
        except (json.JSONDecodeError, ValueError) as error:
            raise ValueError(f"{path}:{number}: {error}") from error
        scenarios[marker["scenario"]].append(tuple(marker[field] for field in FIELDS[1:]))
    if not scenarios:
        raise ValueError(f"{path}: no STREG markers found")
    return dict(scenarios)


def compare(before, after):
    differences = []
    for scenario in sorted(before.keys() | after.keys()):
        old = [" / ".join(row) for row in before.get(scenario, [])]
        new = [" / ".join(row) for row in after.get(scenario, [])]
        if old != new:
            differences.append({"scenario": scenario, "diff": list(difflib.unified_diff(old, new, fromfile="baseline", tofile="current", lineterm=""))})
    return differences


def main(argv=None):
    parser = argparse.ArgumentParser(description="Compare StateTree scenario markers from two Unreal logs")
    parser.add_argument("baseline")
    parser.add_argument("current")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    try:
        differences = compare(read_markers(args.baseline), read_markers(args.current))
    except (OSError, ValueError) as error:
        parser.error(str(error))
    if args.json:
        print(json.dumps(differences, indent=2, ensure_ascii=False))
    elif not differences:
        print("All StateTree scenarios match the baseline.")
    else:
        for difference in differences:
            print(f"Scenario: {difference['scenario']}")
            print("\n".join(difference["diff"]))
    return int(bool(differences))


if __name__ == "__main__":
    raise SystemExit(main())
