from pathlib import Path

from csv_sum_cli.cli import sum_amounts


def test_sum_amounts(tmp_path: Path) -> None:
    csv_file = tmp_path / "sample.csv"
    csv_file.write_text(
        "date,amount\n"
        "2025-01-01,100\n"
        "2025-01-02,250\n",
        encoding="utf-8",
    )

    assert sum_amounts(csv_file) == 350
