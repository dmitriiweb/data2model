import pathlib

import aiofiles


async def read_file(filepath: pathlib.Path) -> str:
    async with aiofiles.open(filepath, "r") as f:
        content = await f.read()
    return content
