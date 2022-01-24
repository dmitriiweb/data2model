import pytest

from data_to_model.type_detectors import SimpleTypeDetector, SimpleTypeNames


@pytest.mark.parametrize(
    "value, expected_type",
    [
        (1, SimpleTypeNames.INTEGER),
        (1.0, SimpleTypeNames.FLOAT),
        ("string", SimpleTypeNames.STRING),
        (True, SimpleTypeNames.BOOLEAN),
        (None, SimpleTypeNames.NONE),
        ("1", SimpleTypeNames.INTEGER),
        ("1.0", SimpleTypeNames.FLOAT),
        ("1.0 ", SimpleTypeNames.FLOAT),
        (" 1.0 ", SimpleTypeNames.FLOAT),
        (" 1.0", SimpleTypeNames.FLOAT),
        ("True", SimpleTypeNames.BOOLEAN),
        ("", SimpleTypeNames.NONE),
    ],
)
def test_simple_type_detector(value, expected_type):
    type_detector = SimpleTypeDetector()
    assert type_detector.detect_type(value) == expected_type


def test_simple_type_detector_error():
    type_detector = SimpleTypeDetector()
    value = [1, 2, 3]
    with pytest.raises(TypeError) as error:
        type_detector.detect_type(value)

    assert "SimpleType" in str(error.value)
