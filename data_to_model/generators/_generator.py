from abc import ABC, abstractmethod
from typing import List

from ._types import ClassData, ClassField


class Generator(ABC):
    """
    Base class for data class generators
    """

    def __init__(self, classes: List[ClassData], file_name: str):
        self.classes = classes
        self.file_name = file_name

    @abstractmethod
    def generate_file_content(self) -> str:
        pass
