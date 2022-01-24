from dataclasses import dataclass
from typing import List

from data_to_model.models.class_field import ClassField


@dataclass
class DataClass:
    name: str
    fields: List[ClassField]
