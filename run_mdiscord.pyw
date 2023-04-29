from main import MDiscord
from status_types import register_all_status
from dotenv import dotenv_values
import getpass
import os
import config


USER_NAME = getpass.getuser()


def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "autostart_mdiscord.bat", "w+") as bat_file:
        bat_file.write('pythonw {1}'.format(file_path, file_path + r"\run_mdiscord.pyw"))



mdiscord = MDiscord(config.TOKEN, config.STATUS)

register_all_status(mdiscord)

add_to_startup()

mdiscord.run()