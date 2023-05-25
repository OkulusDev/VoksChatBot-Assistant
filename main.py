#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Голосовой ассистент Вокс - быстрый, полезный и функциональный
Создатель: OkulusDev (C) 2023
Лицензия: GNU GPL v3"""
import json
from tkinter import *
from voice import TTS
from awesometerm import msg, Logger
from assistant import Assistant

BG_GRAY = "#353535"
BG_COLOR = '#101010'
FG_COLOR = '#b8b8b8'
FONT = 'Sans 14'
FONT_BOLD = 'Sans 14 bold'


class ChatBotApp:
	def __init__(self, assistant, voice):
		self.window = Tk()
		self.assistant = assistant
		self.voice = voice
		self.__setup_window()

	def run(self):
		self.window.mainloop()

	def __setup_window(self):
		self.window.title("Чатбот-ассистент Вокс")
		self.window.resizable(False, False)
		self.window.configure(width=550, height=600, bg=BG_COLOR)

		title_label = Label(self.window, bg=BG_COLOR, fg=FG_COLOR, font=FONT,
							text='Чатбот-ассистент Вокс')
		title_label.place(relwidth=1, relheight=0.08)

		line_hr = Label(self.window, width=450, bg=BG_GRAY)
		line_hr.place(relwidth=1, rely=0.07, relheight=0.012)

		self.text_widget = Text(self.window, width=20, height=2,
								bg=BG_COLOR, fg=FG_COLOR, 
								font=FONT, padx=5, pady=5)
		self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
		self.text_widget.configure(cursor='arrow', state=DISABLED)

		end_label = Label(self.window, bg=BG_GRAY, fg=FG_COLOR, height=80)
		end_label.place(relwidth=1, rely=0.825)

		self.msg_entry = Entry(end_label, bg='#b8b8b8', fg='#050505', font=FONT)
		self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
		self.msg_entry.focus()
		self.msg_entry.bind("<Return>", self.__on_enter_pressed)

		send_button = Button(end_label, bg='#10893e', fg='#fff', 
							font=FONT_BOLD, text='Отправить', width=20,
							command=lambda: self.__on_enter_pressed(None))
		send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

	def __on_enter_pressed(self, event):
		msg_text = self.msg_entry.get()
		self.insert_message(msg_text, "Вы")
		bot_answer = self.assistant.get_response(msg_text)
		self.voice.say(bot_answer)
		self.insert_message(bot_answer, f'{self.assistant.name}')

	def insert_message(self, msg, sender):
		if not msg:
			return

		self.msg_entry.delete(0, END)
		first_msg = f'[{sender}] {msg}\n'

		self.text_widget.configure(state=NORMAL)
		self.text_widget.insert(END, first_msg)
		self.text_widget.configure(state=DISABLED)


def main():
	logger = Logger()
	
	with open("config.json", "r") as read_file:
		logger.info('Successfully load config')
		config = json.load(read_file)

	tts = TTS(config["name"], config)
	bot = Assistant(config["name"])

	bot.load_phrases('phrases.json')
	logger.info('Successfully load phrases')

	app = ChatBotApp(bot, tts)
	app.run()


if __name__ == '__main__':
	main()
