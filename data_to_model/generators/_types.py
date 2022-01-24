from typing import List, Protocol


class ClassField(Protocol):
    name: str
    original_name: str
    type: str


class ClassData(Protocol):
    name: str
    fields: List[ClassField]

    def get_types_for_import(self) -> List[str]:
        ...
