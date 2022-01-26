import pathlib

from collections import defaultdict
from typing import AsyncGenerator, Dict, List, Optional

import aiofiles

from aiocsv import AsyncDictReader
from data_to_model.data_parsers.data_parser import DataParser
from data_to_model.models import ClassData
from data_to_model.type_detectors import TypeDetector

from .types import Collection


class CsvDataParser(DataParser):
    async def from_file(
        self,
        file_path: pathlib.Path,
        root_class_name: Optional[str] = None,
        **kwargs,
    ) -> List[ClassData]:
        delimiter = kwargs.get("delimiter", ",")
        all_types = defaultdict(set)

        type_detector = TypeDetector()
        async for row in self.read_csv(file_path, delimiter):
            for k, v in row.items():
                detected_type = type_detector.from_value(v)
                all_types[k].add(detected_type)

        return []

    def from_collection(
        self, collection: Collection, root_class_name: str
    ) -> List[ClassData]:
        pass

    @staticmethod
    async def read_csv(
        file_path: pathlib.Path, delimiter: str = ","
    ) -> AsyncGenerator[Dict[str, str], None]:
        async with aiofiles.open(
            file_path, mode="r", encoding="utf-8", newline=""
        ) as f:
            async for row in AsyncDictReader(f, delimiter=delimiter):
                yield row