from abc import ABC, abstractmethod

from data_to_model.type_detectors._types import DataType


class BaseDetector(ABC):
    @abstractmethod
    def detect_type(self, value: DataType) -> str:
        pass
