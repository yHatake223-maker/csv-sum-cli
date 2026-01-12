from __future__ import annotations

import csv
import sys
from pathlib import Path


def sum_amounts(csv_path: Path) -> int:
    total = 0
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            raw = row["amount"]
            try:
                total += int(raw)
            except (TypeError, ValueError):
                print(f"WARNING: Skipping non-numeric amount: {raw}", file=sys.stderr)
    return total
