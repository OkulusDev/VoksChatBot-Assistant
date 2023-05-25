#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Микро-библиотека AwesomeTerm для вывода последовательности ANSI кодов для форматирования текста
Создатель: OkulusDev (C) 2023 ALL RIGHTS REVERSED
Лицензия: GNU GPL v3"""
import sys
import os
import logging

__author__ = 'OkulusDev'


def cls():
	# Очистка терминала
	os.system('clear')


class Logger:
	def __init__(self):
		logging.basicConfig(level=logging.INFO,
							filename="assistant.log", filemode="w",
							format="(%(asctime)s) [%(levelname)s] %(message)s")	

	def info(self, text):
		logging.info(text)

	def warn(self, text):
		logging.warn(text)

	def error(self, text):
		logging.error(text)

	def debug(self, text):
		logging.debug(text)


class Fore:
	# Фоновый цвет текста
	black = '\033[30m'					# Черный
	red = '\033[31m'					# Красный
	green = '\033[32m'					# Зеленый
	yellow = '\033[33m'                 # Желтый
	blue = '\033[34m'					# Синий
	magenta = '\033[35m'				# Фиолетовый
	cyan = '\033[36m'					# Бирюзовый
	white = '\033[37m'					# Белый


class Style:
	# Стиль текста
	bold = '\033[1m'					# Жирный
	light = '\033[2m'					# Легкий
	cursive = '\033[3m'					# Курсив
	underline = '\033[4m'				# Подчеркнутый
	blinked = '\033[5m'					# Мигающий
	lined = '\033[9m'					# Перечеркнутый
	end = '\033[0m'						# Конец строки, сброс стилей


def msg(self, text, msg_type):
	style = Style()
	fore = Fore()

	if msg_type.lower() == 'info':
		return f'{fore.green}[INFO]{style.end}{style.bold} {text}{style.end}'
	elif msg_type.lower() == 'warning':
		return f'{fore.yellow}[WARNING]{style.end}{style.bold} {text}'
	elif msg_type.lower() == 'error':
		return f'{fore.red}[ERROR]{style.end}{style.bold} {text}'
