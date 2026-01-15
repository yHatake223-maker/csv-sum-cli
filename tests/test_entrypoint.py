import subprocess
import sys
from pathlib import Path


def test_cli_skips_nonnumeric_and_prints_warning(tmp_path: Path):
    csv = tmp_path / "sample.csv"
    csv.write_text(
        "date,amount\n"
        "2025-01-01,100\n"
        "2025-01-02,abc\n"
        "2025-01-03,250\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        [sys.executable, "-m", "csv_sum_cli", str(csv)],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "Total amount: 350" in result.stdout
    assert "Skipping non-numeric amount" in result.stderr
