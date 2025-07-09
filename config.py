from configparser import ConfigParser
from typing import TypedDict, List

class Client(TypedDict):
    name: str
    token: str
    text: str
    separator: str = "&"

def read_config(file: str = "config.ini") -> ConfigParser:
    config = ConfigParser()
    config.read(file)
    return config

def get_delay(file: str = "config.ini") -> float:
    config = read_config(file=file)
    return config.getfloat("settings", "delay") or 4.0

def get_clients(file: str = "config.ini") -> List[Client]:
    config = read_config(file=file)
    clients = config.get("settings", "clients").split(" ")
    for client in clients:
        section = f"client/{client}"
        token = config.get(section, "token")
        text = config.get(section, "text")
        separator = config.get(section, "separator", fallback=None) or "&"
        clients.remove(client)
        clients.append(Client(name=client, token=token, text=text, separator=separator))
    return clients