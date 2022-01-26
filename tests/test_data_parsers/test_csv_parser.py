import pathlib

import pytest

from data_to_model.data_parsers import CsvDataParser


@pytest.mark.skip("Need to finish method")
async def test_from_file(csv_test_file: pathlib.Path):
    parser = CsvDataParser()
    data_classes = await parser.from_file(csv_test_file)
    data_class = data_classes[0]

    assert data_class.name == "Example"

    for field in data_class.fields:
        if field.name.replace("\ufeff", "") == "col1":
            assert field.type == "int"
        elif field.name == "col2":
            assert field.type == "Optional[float]"
        elif field.name == "col3":
            assert field.type == "Union[str, float]"


async def test_from_collection():
    pass
