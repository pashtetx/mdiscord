from config import get_clients
from queries import token_validate, change_custom_status

import logging
import asyncio

async def worker(token: str, text: str, separator: str) -> None:
    while True:
        for part in text.split(separator):
            await asyncio.sleep(3)
            await change_custom_status(token=token, text=part)

async def main() -> None:
    clients = get_clients()
    for client in clients:
        if not await token_validate(client["token"]):
            name = client["name"]
            logging.warning(f"Client {name} has not valid token!")
            clients.remove(client)
    await asyncio.gather(
        *[
            worker(
                token=client["token"], 
                text=client["text"], 
                separator=client["separator"]
            ) for client in clients
        ]
    )

if __name__ == "__main__":
    asyncio.run(main())