import pathlib

from enum import Enum, auto
from typing import Union

from .data_parser import DataParser


class SupportedDataTypes(Enum):
    CSV = auto()

    @classmethod
    def from_path(cls, path: pathlib.Path) -> "SupportedDataTypes":
        if path.suffix in {".csv", ".tsv", ".txt"}:
            return cls.CSV
        raise ValueError(f"Unsupported file type: {path.suffix}")


class DataParserFactory:
    @staticmethod
    def get_parser(data_type: Union[SupportedDataTypes, pathlib.Path]) -> DataParser:
        if isinstance(data_type, pathlib.Path):
            data_type = SupportedDataTypes.from_path(data_type)

        if data_type == SupportedDataTypes.CSV:
            from .csv_parser import CsvDataParser

            return CsvDataParser()
        else:
            raise ValueError("Data type not supported")
