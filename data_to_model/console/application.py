"""
# Usage:

data2model -if data.csv -of data.py
"""
import argparse

from dataclasses import dataclass
from pathlib import Path


@dataclass()
class Arguments:
    input_file: Path
    output_file: Path


def get_user_args() -> Arguments:
    parser = argparse.ArgumentParser(
        description="Convert data file (csv, json etc. to Python model"
    )
    parser.add_argument(
        "-if",
        "--input-file",
        type=str,
        required=True,
        help="Input file, e.g. data.csv",
    )
    parser.add_argument(
        "-of",
        "--output-file",
        type=str,
        required=True,
        help="Output file, e.g. data.py",
    )

    args = parser.parse_args()

    return Arguments(
        input_file=Path(args.input_file), output_file=Path(args.output_file)
    )


def main():
    user_args = get_user_args()


if __name__ == "__main__":
    main()
