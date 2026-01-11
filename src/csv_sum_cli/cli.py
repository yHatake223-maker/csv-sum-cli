from __future__ import annotations

import csv
from pathlib import Path


def sum_amounts(csv_path: Path) -> int:
    total = 0
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total += int(row["amount"])
    return total
