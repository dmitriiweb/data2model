import pytest

from data_to_model.type_detectors import TypeDetector, TypeNames


@pytest.mark.parametrize(
    "value, expected_type",
    [
        (1, TypeNames.INTEGER),
        (1.0, TypeNames.FLOAT),
        ("string", TypeNames.STRING),
        (True, TypeNames.BOOLEAN),
        (None, TypeNames.NONE),
        ("1", TypeNames.INTEGER),
        ("1.0", TypeNames.FLOAT),
        ("1.0 ", TypeNames.FLOAT),
        (" 1.0 ", TypeNames.FLOAT),
        (" 1.0", TypeNames.FLOAT),
        ("True", TypeNames.STRING),
        ("", TypeNames.NONE),
    ],
)
def test_simple_type_detector(value, expected_type):
    assert TypeDetector.from_value(value) == expected_type


def test_simple_type_detector_error():
    value = [1, 2, 3]
    with pytest.raises(TypeError) as error:
        TypeDetector.from_value(value)

    assert "SimpleType" in str(error.value)


@pytest.mark.parametrize(
    "types, expected_type",
    [
        ({TypeNames.INTEGER}, "int"),
        ({TypeNames.INTEGER, TypeNames.FLOAT}, "Union[float, int]"),
        ({TypeNames.NONE}, "Optional"),
        ({TypeNames.NONE, TypeNames.INTEGER}, "Optional[int]"),
        (
            {TypeNames.NONE, TypeNames.INTEGER, TypeNames.FLOAT},
            "Optional[Union[float, int]]",
        ),
        ({TypeNames.INTEGER, "CustomType"}, "Union[CustomType, int]"),
    ],
)
def test_from_dict(types, expected_type):
    type_detector = TypeDetector()
    assert type_detector.from_set(types) == expected_type
