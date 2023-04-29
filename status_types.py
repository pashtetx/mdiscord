from main import MDiscord
from datetime import datetime
from time import sleep


def time(delay, set_status_callback) -> None:
	while True:
		set_status_callback(datetime.now().strftime("Сейчас: %H:%M"))
		sleep(delay)



def music_text(delay, set_status_callback) -> None:
	
	text = """
		Сломанный ублюдок, я родился в рефлексии
		If you wanna be a bitch, then I never wanna see ya
		Я поставил ей диагноз — необходимость в терапии
		All 'em people need us, 'cause they know I'm a playa
		Отражение во снах твоих, я сонный паралич
		Моё касание летально, в сердце холод, будто Lich
		Я порезался о стёкла, почему не вижу лиц?
		В себе новое отличие я раздвоил, будто глитч
		Как к тебе я отношусь — в твоём обличии очнусь
		Снова мой метаморфоз, меня мучает невроз
		Поток угроз, страхе ловишь передоз, экран не показывает пульс
		Скоро будет рост, скорость замедляет дождь, себя ощущаю lost
		I can be a ghost, сука
		I am never close, yeah
		I can do the most, girl
		Meta-metamorphosis
		Never stoppin' for a second
		Gonna die like a red rose, black rosе, fuck hoes?
		N-N-Never overdose, I'm a wild rose, white rose
		Feelin' comatose I wanna cut throats — Death Row
		Мир, заточенный во лжи, снова сбил себе режим
		Тебе хочется уйти, сука, просто не дыши
		Расскажи, кем дорожишь, сука, тише, тише
		Тише, тише, тише
	"""

	parse_string = text.split("\n")

	counter = 0

	while True:
		try:
			set_status_callback(parse_string[counter])
			counter += 1
		except IndexError:
			counter = 0
		sleep(delay)







def register_all_status(mdsicord: MDiscord):
	mdsicord.add_status(time,"time")
	mdsicord.add_status(music_text,"music")