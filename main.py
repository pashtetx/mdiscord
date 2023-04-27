from time import sleep
from json import dumps
import requests
import datetime
import random


class Main():

	def __init__(self, token, select):

		self.headers = {"authorization": token, "content-type": "application/json"}
		self.url = 'https://discord.com/api/users/@me/settings'
		self.delay = 4

		self.status_list = {
			"time":self.time,
			"loading":self.loading,
			"ghoul":self.ghoul,
		}



		self.select_status(select)

	def select_status(self, select: str) -> None:
		for k, v in self.status_list.items():
			if k.lower() == select:
				v()
				break


	def get_delay(self):

		return random.randint(self.delay - 1, self.delay)

	def set_status(self, status: str) -> None:
		res = requests.patch(self.url, headers = self.headers, data = dumps({'custom_status': {'text':status}}))
		print(res)

 
	def ghoul(self): # ghoul

		i = 6

		while i > 0:
			self.set_status(f"{i} - 7 = {i - 7}")
			i = i - 7
			if i < 0:
				i = 1000
				self.set_status("Я гуль")
			sleep(self.get_delay())

	def loading(self): # loading
		
		i = 1

		while i <= 10:
			self.set_status(("#" * i) + "-" * (10 - i) + f" {i}0%")
			sleep(self.get_delay())
			i += 1
			if i == 10:
				i = 1
				self.set_status("Какой-то текст")
				sleep(self.get_delay())


	def time(self): # time

		while True:
			print(self.get_delay())
			self.set_status(datetime.datetime.now().strftime("%H:%M")) # Set status formated now datetime.
			sleep(self.get_delay())

