import pathlib

from dataclasses import dataclass


@dataclass()
class DataClassModel:
    content: str

    async def save(self, filepath: pathlib.Path) -> None:
        pass
