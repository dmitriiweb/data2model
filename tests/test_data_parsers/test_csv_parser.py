import pathlib

from data_to_model.data_parsers import CsvDataParser


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
            assert field.type == "str"


async def test_from_collection(csv_test_file: pathlib.Path):
    data = []
    async for row in CsvDataParser.read_csv(csv_test_file):
        data.append(row)

    parser = CsvDataParser()
    data_classes = parser.from_collection(data, "Example")
    data_class = data_classes[0]

    assert data_class.name == "Example"

    for field in data_class.fields:
        if field.name.replace("\ufeff", "") == "col1":
            assert field.type == "int"
        elif field.name == "col2":
            assert field.type == "Optional[float]"
        elif field.name == "col3":
            assert field.type == "str"
