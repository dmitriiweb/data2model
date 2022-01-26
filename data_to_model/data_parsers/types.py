from typing import Any, Dict, List, Union

from data_to_model.type_detectors.types import SimpleType


CsvDataType = List[Dict[str, SimpleType]]
JsonDataType = Dict[str, Any]
Collection = Union[CsvDataType, Dict]
