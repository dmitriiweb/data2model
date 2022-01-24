from typing import List

import pytest

from data_to_model.models.class_data import ClassData
from data_to_model.models.class_field import ClassField


@pytest.fixture()
def class_fields() -> List[ClassField]:
    fields_data = [
        {"name": "field1", "type": "int", "original_name": "Field1"},
        {"name": "field2", "type": "float", "original_name": "Field2"},
        {"name": "field3", "type": "bool", "original_name": "Field3"},
        {"name": "field4", "type": "str", "original_name": "Field4"},
    ]
    return [ClassField(**i) for i in fields_data]


@pytest.fixture()
def data_class(class_fields) -> ClassData:
    return ClassData(name="TestClass", fields=class_fields)
