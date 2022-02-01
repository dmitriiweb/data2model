import pytest

from data_to_model.name_formatters import SnakeCaseFormatter


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("name", "name"),
        ("Name", "name"),
        ("NameName", "name_name"),
        ("nameName", "name_name"),
        ("+45Name", "_45_name"),
        ("45name", "_45name"),
        ("name name", "name_name"),
        ("name-name", "name_name"),
        ("NNNameNNameName", "nnn_ame_nn_ame_name"),
        ("namE", "name"),
        ("name45", "name45"),
    ],
)
def test_name(input_string, expected_output):
    formatter = SnakeCaseFormatter(input_string)
    assert formatter.format() == expected_output
