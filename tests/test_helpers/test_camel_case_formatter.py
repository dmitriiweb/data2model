import pytest

from data_to_model.helpers import CamelCaseFormatter


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("file_name", "FileName"),
        ("FileName", "FileName"),
        ("file name", "FileName"),
        ("file.name", "FileName"),
    ],
)
def test_camel_case_formatter(input_string, expected_output):
    formatter = CamelCaseFormatter(input_string)
    assert formatter.format() == expected_output
