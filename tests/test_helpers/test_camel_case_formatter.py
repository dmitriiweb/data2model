import pytest

from data_to_model.name_formatters import CamelCaseFormatter


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("file_name", "FileName"),
        ("1file_name", "_1fileName"),
        ("FileName", "FileName"),
        ("file name", "FileName"),
        ("file.name", "FileName"),
        ("file+name3", "FileName3"),
    ],
)
def test_camel_case_formatter(input_string, expected_output):
    formatter = CamelCaseFormatter(input_string)
    assert formatter.format() == expected_output
