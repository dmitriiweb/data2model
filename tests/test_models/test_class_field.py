import pytest

from data_to_model.models import ClassField


@pytest.mark.parametrize(
    "original_name, expected_name",
    [
        ("name", "name"),
        ("Name", "name"),
        ("NameName", "name_name"),
        ("nameName", "name_name"),
        ("NNNameNNameName", "nnn_ame_nn_ame_n_ame"),
        ("+45Name", "_45name"),
        ("45name", "_45name"),
    ],
)
def test_name(original_name, expected_name):
    class_field = ClassField(original_name=original_name, type="")
    assert class_field.name == expected_name
