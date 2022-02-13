"""
# Usage:

data2model -if data.csv -of data.py
"""
import argparse
import asyncio

from pathlib import Path

import asyncclick as click


@click.command()
@click.option(
    "-if", "--input-file", type=str, required=True, help="Input file, e.g. data.csv"
)
@click.option(
    "-of", "--output-file", type=str, required=True, help="Output file, e.g. data.py"
)
async def model_generator(input_file, output_file):
    print(input_file)
    print(output_file)


def main():
    model_generator(_anyio_backend="asyncio")


if __name__ == "__main__":
    main()
