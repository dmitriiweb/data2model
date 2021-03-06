# data2model

![kdpv](https://github.com/dmitriiweb/data2model/raw/main/imgs/matrix-g69866a888_640.jpg)

![Tests](https://github.com/mCodingLLC/SlapThatLikeButton-TestingStarterProject/actions/workflows/tests.yml/badge.svg)
[![PyPI version](https://badge.fury.io/py/data2model.svg)](https://badge.fury.io/py/data2model)

Python library and CLI tool for generating different Python data classes from data.

Supported data formats:
- CSV

Supported data classes:
- [dataclasses](https://docs.python.org/3.8/library/dataclasses.html)

## Requirements

- Python 3.8+

## Installation
```shell
pip install data2model
```

## Usage

### As library
```python
import asyncio
import pathlib

from data_to_model import ModelGenerator


files = [
    {"input": pathlib.Path("example.csv"), "output": pathlib.Path("example.py")},
]


async def model_generator(input_file: pathlib.Path, output_file: pathlib.Path):
    mg = ModelGenerator(input_file)
    model = await mg.get_model()
    await model.save(output_file)


async def main():
    tasks = [model_generator(i["input"], i["output"]) for i in files]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
```
![output](https://github.com/dmitriiweb/data2model/raw/main/imgs/carbon.png)


### As CLI
#### from single file
```shell
$ cat data.csv
col1,col2
1,2
,2.0

$ data2model file -if data.csv -of data.py
$ cat data.py
# This file was generated by data_to_model.
from dataclasses import dataclass
from typing import Any, Dict, Optional, Union


@dataclass
class Data:
    col1: Optional[int]
    col2: Union[float, int]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Data":
        col1 = data["col1"]
        col2 = data["col2"]
        return cls(col1=col1, col2=col2)

    def to_dict(self) -> Dict[str, Any]:
        return {"col1": self.col1, "col2": self.col2}
```

#### from directory
```shell

$ data2model folder -if data -of models

$ ls data
data1.csv  data2.csv

$ ls models
data1.py  data2.py
```