import requests

API_URL = "https://discord.com/api/v9/"
SETTINGS_ENDPOINT = API_URL + "users/@me/settings"
ME_ENDPOINT = API_URL + "users/@me"

def generate_headers(token: str, content_type: str = "application/json") -> dict:
    return {
        "Authorization":token,
        "Content-type":content_type
    }

def change_custom_status(token: str, text: str) -> requests.Response:

    return requests.patch(SETTINGS_ENDPOINT, headers=generate_headers(token), json={
        "custom_status":{
            "text":text,
        }
    })

def token_validate(token: str) -> bool:
    return requests.get(ME_ENDPOINT, headers=generate_headers(token)).status_code == 200