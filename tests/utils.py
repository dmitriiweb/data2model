import pathlib

from typing import Dict, List

import aiocsv
import aiofiles


async def read_file(filepath: pathlib.Path) -> str:
    async with aiofiles.open(filepath, "r") as f:
        content = await f.read()
    return content


async def read_csv(filepath: pathlib.Path) -> List[Dict[str, str]]:
    rows = []
    async with aiofiles.open(filepath, "r") as f:
        async for row in aiocsv.AsyncDictReader(f):
            rows.append(row)
    return rows
