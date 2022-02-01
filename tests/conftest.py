import pathlib

from typing import List

import pytest

from data_to_model.models import ClassData, ClassField


DATA_FILES = pathlib.Path(__file__).parent / "data_files"


@pytest.fixture()
def csv_test_file() -> pathlib.Path:
    return DATA_FILES / "example.csv"


@pytest.fixture()
def class_fields_simple() -> List[ClassField]:
    fields_data = [
        {"type": "int", "original_name": "Field1"},
        {"type": "float", "original_name": "Field2"},
        {"type": "bool", "original_name": "Field3"},
        {"type": "str", "original_name": "Field4"},
        {"type": "List", "original_name": "Field5"},
    ]
    return [ClassField(**i) for i in fields_data]


@pytest.fixture()
def data_class_simple(class_fields_simple) -> ClassData:
    return ClassData(name="TestClass", fields=class_fields_simple)


@pytest.fixture()
def class_fields_different_types() -> List[ClassField]:
    fields_data = [
        {"type": "int", "original_name": "Field1"},
        {"type": "float", "original_name": "Field2"},
        {"type": "bool", "original_name": "Field3"},
        {"type": "str", "original_name": "Field4"},
        {"type": "List", "original_name": "Field5"},
        {"type": "Optional[int]", "original_name": "Field6"},
        {"type": "Dict[str, Any]", "original_name": "Field6"},
    ]
    return [ClassField(**i) for i in fields_data]


@pytest.fixture()
def data_class_different_types(class_fields_different_types) -> ClassData:
    return ClassData(name="TestClass", fields=class_fields_different_types)
