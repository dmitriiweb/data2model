from enum import Enum, auto
from typing import List

from .base_generator import BaseGenerator
from .dataclass_generator import DataClassGenerator
from .types import ClassData


class SupportedDataClasses(Enum):
    PythonDataClass = auto()


DATA_CLASSES = {SupportedDataClasses.PythonDataClass: DataClassGenerator}


class GeneratorFactory:
    @staticmethod
    def get_generator(
        data_class: SupportedDataClasses, classes: List[ClassData], file_name: str
    ) -> BaseGenerator:
        try:
            return DATA_CLASSES[data_class](classes, file_name)
        except KeyError:
            raise NotImplementedError(f"{data_class} is not supported")
