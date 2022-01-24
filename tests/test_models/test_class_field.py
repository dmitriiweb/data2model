import pytest

from data_to_model.models import ClassField


@pytest.mark.parametrize(
    "original_name, expected_name",
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
def test_name(original_name, expected_name):
    class_field = ClassField(original_name=original_name, type="")
    assert class_field.name == expected_name
