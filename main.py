from time import sleep
from json import dumps
import requests



class Main():

	def __init__(self, token, select):

		self.headers = {"authorization": token, "content-type": "application/json"}
		self.url = 'https://discord.com/api/users/@me/settings'
		self.delay = 4

		if select == 'ghoul':
			self.ghoul()
		elif select == 'loading':
			self.loading()

	def set_status(self, status):
		res = requests.patch(self.url, headers = self.headers, data = dumps({'custom_status': {'text':status}}))
		print(res.json())


	def ghoul(self):

		i = 6

		while i > 0:
			self.set_status(f"{i} - 7 = {i - 7}")
			i = i - 7
			if i < 0:
				i = 1000
				self.set_status("Я гуль")
			sleep(self.delay)

	def loading(self):
		
		i = 1

		while i <= 10:
			self.set_status(("#" * i) + "-" * (10 - i) + f" {i}0%")
			sleep(self.delay)
			i += 1
			if i == 10:
				i = 1
				self.set_status("Какой-то текст")
				sleep(self.delay)




bot = Main("your token here", "status type here")
