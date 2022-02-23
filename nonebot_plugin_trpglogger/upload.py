from pathlib import Path
from httpx import AsyncClient
import aiofiles


async def upload_file(log_path: Path):
    async with aiofiles.open(log_path, "rb") as f:
        async with AsyncClient() as client:
            resp = await client.post(
                "http://api.dice.center/dicelogger/",
                data={"name": log_path.name},
                files={"file": await f.read()},
            )
            print(resp.text)