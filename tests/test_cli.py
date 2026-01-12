from pathlib import Path

from csv_sum_cli.cli import sum_amounts


def test_sum_amounts(tmp_path: Path) -> None:
    csv_file = tmp_path / "sample.csv"
    csv_file.write_text(
        "date,amount\n2025-01-01,100\n2025-01-02,250\n",
        encoding="utf-8",
    )

    assert sum_amounts(csv_file) == 350


def test_sum_amounts_skips_non_numeric(tmp_path: Path) -> None:
    csv_file = tmp_path / "sample.csv"
    csv_file.write_text(
        "date,amount\n2025-01-01,100\n2025-01-02,abc\n2025-01-03,250\n",
        encoding="utf-8",
    )

    assert sum_amounts(csv_file) == 350
