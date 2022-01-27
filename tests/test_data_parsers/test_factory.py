import pathlib

import pytest

from data_to_model.data_parsers import CsvDataParser, DataParser, DataParserFactory


@pytest.mark.parametrize(
    "path, expected_parser",
    [
        (pathlib.Path("example.csv"), CsvDataParser),
        (pathlib.Path("example.tsv"), CsvDataParser),
        (pathlib.Path("example.txt"), CsvDataParser),
    ],
)
def test_factory(path: pathlib.Path, expected_parser: DataParser):
    parser = DataParserFactory.get_parser(path)
    assert isinstance(parser, expected_parser)
