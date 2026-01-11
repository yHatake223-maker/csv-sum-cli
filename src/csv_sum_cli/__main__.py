from __future__ import annotations

import argparse
from pathlib import Path

from .cli import sum_amounts


def main() -> None:
    parser = argparse.ArgumentParser(description="Sum amounts from a CSV file.")
    parser.add_argument("csv_path", type=Path)
    args = parser.parse_args()

    total = sum_amounts(args.csv_path)
    print(f"Total amount: {total}")


if __name__ == "__main__":
    main()
