from abc import ABC, abstractmethod

from .types import SimpleType


class BaseDetector(ABC):
    @abstractmethod
    def detect_type(self, value: SimpleType) -> str:
        pass
