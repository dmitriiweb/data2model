from abc import ABC, abstractmethod

from data_to_model.type_detectors._types import SimpleType


class BaseDetector(ABC):
    @abstractmethod
    def detect_type(self, value: SimpleType) -> str:
        pass
