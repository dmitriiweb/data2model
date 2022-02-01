import pathlib

import pytest

from data_to_model import ModelGenerator
from data_to_model.data_parsers.types import SupportedDataTypes
from data_to_model.generators.types import SupportedDataClasses

import tests.utils as utils


DATA_FOLDER = pathlib.Path(__file__).parent.joinpath("data_files")


pytest.mark.parametrize("filepath, output_filepath")
csv1 = DATA_FOLDER.joinpath("example.csv")
csv3 = DATA_FOLDER.joinpath("example.txt")
csv4 = DATA_FOLDER.joinpath("example_tabs.csv")

output = DATA_FOLDER.joinpath("output_example_csv.txt")


@pytest.mark.parametrize(
    "filepath, output_filepath",
    [
        (csv1, output),
        (csv3, output),
        (csv4, output),
    ],
)
async def test_model_generator_from_csv(
    filepath: pathlib.Path, output_filepath: pathlib.Path
):
    output_text = await utils.read_file(output_filepath)
    output_text = output_text.strip()

    g = ModelGenerator(filepath, py_dataclass_type=SupportedDataClasses.PythonDataClass)

    if "tabs" in filepath.name:
        g = ModelGenerator(
            filepath,
            py_dataclass_type=SupportedDataClasses.PythonDataClass,
            csv_delimiter="\t",
        )
    else:
        g = ModelGenerator(
            filepath, py_dataclass_type=SupportedDataClasses.PythonDataClass
        )

    res = await g.get_model()

    if "example_tabs.csv" in filepath.name:
        assert "ExampleTabs" in res.content
        res.content = res.content.replace("ExampleTabs", "Example")

    assert res.content.strip() == output_text


async def test_model_generator_from_collection():
    input_data = await utils.read_csv(csv1)
    g = ModelGenerator(
        input_data,
        py_dataclass_type=SupportedDataClasses.PythonDataClass,
        data_type=SupportedDataTypes.CSV,
        root_class_name="Example",
    )
    output_text = await utils.read_file(output)
    output_text = output_text.strip()

    model = await g.get_model()

    assert model.content.strip() == output_text
