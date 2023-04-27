from main import Main
from dotenv import load_dotenv, dotenv_values
import os


CONFIG = dotenv_values(".env")
USERNAME = os.getlogin()


def on_startup(): 
	script_file = os.path.dirname(os.path.realpath(__file__)) + "\\run.pyw"
	startup_dir = os.path.dirname(r"C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\\".format(USERNAME))
	f = open(startup_dir + "\\start.bat", "w")
	f.write(f'pythonw {script_file}')
	f.close()


def del_startup():
	script_file = os.path.dirname(os.path.realpath(__file__)) + "\\run.pyw"
	startup_dir = os.path.dirname(r"C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\\".format(USERNAME))
	os.remove(startup_dir + "\\start.bat")


if CONFIG["AUTOSTART"].lower() == "true":
	on_startup()
else:
	try:
		del_startup()
	except Exception:
		pass



bot = Main(CONFIG["TOKEN"], CONFIG["STATUS_TYPE"])