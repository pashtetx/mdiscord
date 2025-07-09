from config import get_clients, get_delay
from queries import token_validate, change_custom_status

import logging
import asyncio

async def worker(token: str, text: str, separator: str, delay: float = 4.0) -> None:
    while True:
        for part in text.split(separator):
            await asyncio.sleep(get_delay())
            response = await change_custom_status(token=token, text=part)
            if response.status_code != 200:
                logging.warn(f"User {token[:7]} dont change the custom status to '{part}'.")

async def main() -> None:
    clients = get_clients()
    for client in clients:
        if not await token_validate(client["token"]):
            name = client["name"]
            logging.warning(f"Client {name} has not valid token!")
            clients.remove(client)
    delay = get_delay()
    await asyncio.gather(
        *[
            worker(
                token=client["token"], 
                text=client["text"], 
                separator=client["separator"],
                delay=delay,
            ) for client in clients
        ]
    )

if __name__ == "__main__":
    asyncio.run(main())