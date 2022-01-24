import pytest

from data_to_model.type_detectors import SimpleTypeDetector


@pytest.mark.parametrize(
    "value, expected_type",
    [
        (1, "int"),
        (1.0, "float"),
        ("string", "str"),
        (True, "bool"),
        (None, "NoneType"),
        ("1", "int"),
        ("1.0", "float"),
        ("1.0 ", "float"),
        (" 1.0 ", "float"),
        (" 1.0", "float"),
        ("True", "bool"),
        ("", "NoneType"),
    ],
)
def test_simple_type_detector(value, expected_type):
    type_detector = SimpleTypeDetector(value)
    assert type_detector.get_type() == expected_type
