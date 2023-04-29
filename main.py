import requests, json


class MDiscord:

	def __init__(self, token, select):

		self.headers = {
			"authorization": token,
			"content-type": "application/json"
		}

		self.select = select
		self.delay = 4


		self.statuses = {

		}

	def _select_status(self, select: str): 

		if self.statuses == {}:
			assert ValueError("Statuses not defined") # если статусы пустые

		for name, status_func in self.statuses.items():
			if select == name:
				status_func(self.delay, self.set_status)

	def set_status(self, status: str, emoji: str = ""):

		res = requests.patch(
			"https://discord.com/api/users/@me/settings",
			 headers = self.headers, 
			 data = json.dumps(
			 	{
			 		"custom_status": {
			 			'text':status,
			 			"emoji_name": emoji
			 		}
			 	})
			 )

		if res.status_code != 200:
			print("Ошибка:", res.status_code)


	def add_status(self, func, name: str) -> None:
		self.statuses[name] = func


	def run(self):
		self._select_status(self.select)

