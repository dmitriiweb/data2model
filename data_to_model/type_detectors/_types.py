from typing import Any, Dict, List, Union


SimpleType = Union[int, float, str, bool, None]

CompositionType = Union[List[Dict[str, SimpleType]], Dict[str, Any]]

DataType = Union[SimpleType, CompositionType]
