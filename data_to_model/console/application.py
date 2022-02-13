"""
# Usage:

data2model -if data.csv -of data.py
"""
import argparse

from dataclasses import dataclass
from pathlib import Path


class Arguments:
    def __init__(self, input_file: Path, output_file: Path):
        self.input_file = input_file
        self.output_file = output_file

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.input_file=}, {self.output_file=})"

    @classmethod
    def get(cls) -> "Arguments":
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

        return cls(input_file=Path(args.input_file), output_file=Path(args.output_file))


def main():
    user_args = Arguments.get()


if __name__ == "__main__":
    main()
