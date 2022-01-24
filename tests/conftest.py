from typing import List

import pytest

from data_to_model.models import ClassData, ClassField


@pytest.fixture()
def class_fields_simple() -> List[ClassField]:
    fields_data = [
        {"name": "field1", "type": "int", "original_name": "Field1"},
        {"name": "field2", "type": "float", "original_name": "Field2"},
        {"name": "field3", "type": "bool", "original_name": "Field3"},
        {"name": "field4", "type": "str", "original_name": "Field4"},
        {"name": "field5", "type": "List", "original_name": "Field5"},
    ]
    return [ClassField(**i) for i in fields_data]


@pytest.fixture()
def data_class_simple(class_fields_simple) -> ClassData:
    return ClassData(name="TestClass", fields=class_fields_simple)


@pytest.fixture()
def class_fields_different_types() -> List[ClassField]:
    fields_data = [
        {"name": "field1", "type": "int", "original_name": "Field1"},
        {"name": "field2", "type": "float", "original_name": "Field2"},
        {"name": "field3", "type": "bool", "original_name": "Field3"},
        {"name": "field4", "type": "str", "original_name": "Field4"},
        {"name": "field5", "type": "List", "original_name": "Field5"},
        {"name": "field6", "type": "Optional[int]", "original_name": "Field6"},
        {"name": "field6", "type": "Dict[str, Any]", "original_name": "Field6"},
    ]
    return [ClassField(**i) for i in fields_data]


@pytest.fixture()
def data_class_different_types(class_fields_different_types) -> ClassData:
    return ClassData(name="TestClass", fields=class_fields_different_types)
