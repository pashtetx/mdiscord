from typing import Dict
from httpx import AsyncClient, Response

API_URL = "https://discord.com/api/v9/"
SETTINGS_ENDPOINT = API_URL + "users/@me/settings"
ME_ENDPOINT = API_URL + "users/@me"

def generate_headers(token: str, content_type: str = "application/json") -> Dict[str, str]:
    return {
        "Authorization":token,
        "Content-type":content_type
    }

async def change_custom_status(token: str, text: str) -> Response:
    payload = {
        "custom_status":{
            "text":text,
        }
    }
    headers = generate_headers(token=token)
    async with AsyncClient(headers=headers) as session:
        return await session.patch(SETTINGS_ENDPOINT, json=payload)

async def token_validate(token: str) -> bool:
    headers = generate_headers(token=token)
    async with AsyncClient(headers=headers) as session:
        return (await session.get(ME_ENDPOINT)).status_code == 200