#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Голосовой ассистент Вокс - быстрый, полезный и функциональный: синтез речи и работа с голосом
Создатель: OkulusDev (C) 2023
Лицензия: GNU GPL v3"""
import os
import json
import pygame
from gtts import gTTS


class TTS:
	"""Класс для синтеза текста в речь при помощи голосовых движков"""
	def __init__(self, name, config):
		self.config = config
		self.name = name

	def say(self, text: str):
		"""Функция для произведения текст в речь
		Аргументы:
		 + text: str - текст"""
		text = text.replace('"', '').replace("'", '')
		if self.config["voice_engine"] == 'festvox':
			os.system(f'echo "{text}" | festival --tts --language russian')
		elif self.config["voice_engine"] == 'espeak':
			os.system(f'espeak-ng -v ru "{text}"')
		elif self.config["voice_engine"] == 'rhvoice':
			os.system(f'echo "{text}" | RHVoice-test -p {self.voice}')
		elif self.config["voice_engine"] == 'gtts':
			speech = gTTS(text=text, lang='ru', slow=False)
			speech.save('tts/voice.mp3')
			pygame.init()
			pygame.mixer.music.load('tts/voice.mp3')
			pygame.mixer.music.play(0)
