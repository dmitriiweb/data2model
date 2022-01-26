from typing import Dict, List, Union

from data_to_model.type_detectors.types import SimpleType


CsvDataType = List[Dict[str, SimpleType]]
Collection = Union[CsvDataType, Dict]
