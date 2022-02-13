"""
# Usage:

data2model -if data.csv -of data.py
"""
import asyncio  # noqa

from functools import wraps
from pathlib import Path

import click

from data_to_model import ModelGenerator


def coro(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))

    return wrapper


@click.group()
def cli():
    pass


@click.command("file")
@click.option(
    "-if", "--input-file", type=str, required=True, help="Input file, e.g. data.csv"
)
@click.option(
    "-of", "--output-file", type=str, required=True, help="Output file, e.g. data.py"
)
@click.option(
    "--csv-delimiter",
    type=str,
    required=False,
    help="Delimiter in CSV files, default coma(',')",
    default=",",
)
@coro
async def from_file(input_file: str, output_file: str, csv_delimiter: str):
    input_path = Path(input_file)
    output_path = Path(output_file)

    mg = ModelGenerator(input_path, csv_delimiter=csv_delimiter)
    model = await mg.get_model()
    await model.save(output_path)


@click.command("folder")
@click.option(
    "-if", "--input-folder", type=str, required=True, help="Folder with data files"
)
@coro
async def from_folder(input_folder: str):
    print(input_folder)


def main():
    # from_file(_anyio_backend="asyncio")
    # from_folder(_anyio_backend="asyncio")
    cli.add_command(from_file)
    cli.add_command(from_folder)
    cli()


if __name__ == "__main__":
    main()
