import pathlib

from typing import List, Optional

from data_to_model.data_parsers.data_parser import DataParser
from data_to_model.models import ClassData

from .types import Collection


class CsvDataParser(DataParser):
    async def from_file(
        self, file_path: pathlib.Path, root_class_name: Optional[str] = None
    ) -> List[ClassData]:
        pass

    def from_collection(
        self, collection: Collection, root_class_name: str
    ) -> List[ClassData]:
        pass
