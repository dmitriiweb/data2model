import pathlib

from abc import ABC, abstractmethod

from data_to_model.models import ClassData

from .types import Collection


class DataParser(ABC):
    @abstractmethod
    def from_file(self, file_path: pathlib.Path) -> ClassData:
        pass

    @abstractmethod
    def from_collection(self, collection: Collection) -> ClassData:
        pass
