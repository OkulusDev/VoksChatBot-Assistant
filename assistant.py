#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Голосовой ассистент Вокс - быстрый, полезный и функциональный: синтез речи и работа с голосом
Создатель: OkulusDev (C) 2023
Лицензия: GNU GPL v3"""
from random import choice, randint
import re
import json
from fuzzywuzzy import fuzz


class Assistant:
	def __init__(self, name="Вокс"):
		self.name = name
		self.alias = self.name.lower()
		self.responses = self.load_phrases('phrases.json')

	def flip_coin(self):
		return choice(['орел', 'решка'])

	def load_phrases(self, filename):
		with open(filename, 'r') as file:
			return json.load(file)

	def run_command(self, commands):
		full_command = ''
		for command in commands:
			full_command += command + ' '

		full_command = full_command.strip().split(self.alias)[1].strip()

		if fuzz.ratio(full_command, 'подбрось монету') > 55:
			return f'На монете выпало: {self.flip_coin()}'
		else:
			return 'Команда не найдена.'

	def get_response(self, user_data):
		split_message = re.split(r'\s+|[,;?!.-]\s*', user_data.lower())
		
		if split_message[0] == self.alias:
			return self.run_command(split_message)

		score_list = []

		for response in self.responses:
			response_score = 0
			required_score = 0
			required_words = response["required_words"]

			if required_words:
				for word in split_message:
					for required_word in required_words:
						for split_word in word.split(' '):
							if fuzz.ratio(split_word, required_word) > 55:
								required_score += 1

			if required_score == len(required_words):
				for word in split_message:
					for word_input in response["user_input"]:
						if fuzz.ratio(word, word_input) > 55:
							response_score += 1

			score_list.append(response_score)

		best_response = max(score_list)
		response_index = score_list.index(best_response)

		if user_data == "":
			return "Пожалуйста, наберите что-то!"

		if best_response != 0:
			return choice(self.responses[response_index]["responses"])

		return self.invalid_response()

	def invalid_response(self):
		answers = [
			"Я вас не понимаю!", "Что вы имели ввиду?", "Я не понял",
			"Если честно, я не понимаю вас от слова совсем", 
			"Пожалуйста попробуйте написать что-то другое",
			"Объясните пожалуйста, что вы имели ввиду?", 
			"Я извиняюсь, но я не могу ответить на это",
			"Я не могу ответить на это, попробуйте написать что-то другое",
			"Ох! Я не понял, что вы хотели сказать!",
			"Можете попробовать перефразировать ваши слова?",
			"Извините, это не входит в мой функционал",
			"О нет! Ваши слова непонятны для меня!",
			"Я не понимаю вашего языка!"
		]

		answer = choice(answers)

		return answer


if __name__ == '__main__':
	bot = Assistant(name='Вокс')
	bot.load_phrases('phrases.json')

	while True:
		msg = input('You >>> ')
		print('Bot >>> ', bot.get_response(msg))
