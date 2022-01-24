from data_to_model.type_detectors._types import DataType
from data_to_model.type_detectors.base_detector import BaseDetector


class SimpleTypeNames:
    INTEGER = "int"
    FLOAT = "float"
    STRING = "str"
    BOOLEAN = "bool"
    NONE = "NoneType"


class SimpleTypeDetector(BaseDetector):
    def detect_type(self, value: DataType) -> str:

        if isinstance(value, bool):
            return SimpleTypeNames.BOOLEAN

        if value is None or value == "":
            return SimpleTypeNames.NONE

        if isinstance(value, int):
            return SimpleTypeNames.INTEGER

        if isinstance(value, float):
            return SimpleTypeNames.FLOAT

        if isinstance(value, str):
            return self.detect_from_string(value)

        raise TypeError(f"Expected SimpleType, got {type(value)}")

    @staticmethod
    def detect_from_string(value: str) -> str:
        if value.isdigit():
            return SimpleTypeNames.INTEGER

        try:
            float(value)
            return SimpleTypeNames.FLOAT
        except ValueError:
            return SimpleTypeNames.STRING
