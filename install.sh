#!/usr/bin/sh
# -*- coding:utf-8 -*-
# Этот скрипт установит зависимости для Okulus Assistant

distro=$(lsb_release --id --short)							# Имя дистрибутива/операционной системы

# Начало установки
echo "Нажмите Enter чтобы начать установку"
read start
clear

# Установка python3
echo "Установить python3? (y/n)"
read installing
if [ $installing = 'y' ]; then
	echo "Установка . . . "
	if [ $distro = "Debian" ]; then
		# Устанавливаем пакет с помощью пакетного менеджера apt (dpkg), если система - debian
		sudo apt install python3
	elif [ $distro = "Arch" ]; then
		# Устанавливаем пакет с помощью пакетного менеджера pacman, если система - arch
		sudo pacman -Sy python3
	elif [ $distro == 'Fedora' ]; then
		# Устанавливаем пакет с помощью пакетного менеджера dnf (rpm), если система - fedora
		sudo dnf install python3
	else
		# Сообщаем пользователю, что его система не поддерживается
		echo "Ваша операционная система ($distro) не поддерживается. Установите python3 самостоятельно."
	fi
fi

# Установка python3-pip
echo "Установить python3-pip? (y/n)"
read installing2
if [ $installing2 = 'y' ]; then
	echo "Установка . . . "
	if [ $distro = "Debian" ]; then
		# Устанавливаем пакет с помощью пакетного менеджера apt (dpkg), если система - debian
		sudo apt install python3-pip
	elif [ $distro = "Arch" ]; then
		# Устанавливаем пакет с помощью пакетного менеджера pacman, если система - arch
		sudo pacman -Sy python-pip
	elif [ $distro = "Fedora" ]; then
		# Устанавливаем пакет с помощью пакетного менеджера dnf (rpm), если система - fedora
		sudo dnf install python3-pip
	else
		# Сообщаем пользователю, что его система не поддерживается
		echo "Ваша операционная система ($distro) не поддерживается. Установите python-pip самостоятельно."
	fi
fi

# Установка festvox-ru, rhvoice, rhvoice-russian, espeak, espeak-ng
echo "Установить голосовые движки? (y/n)"
read installing2
if [ $installing2 = 'y' ]; then
	echo "Установка . . . "
	if [ $distro = "Debian" ]; then
		# Устанавливаем пакет с помощью пакетного менеджера apt (dpkg), если система - debian
		sudo apt install festvox-ru espeak espeak-ng rhvoice rhvoice-russian
	elif [ $distro = "Arch" ]; then
		# Устанавливаем пакет с помощью пакетного менеджера pacman, если система - arch
		sudo pacman -Sy festvox-ru espeak espeak-ng rhvoice rhvoice-russian
	elif [ $distro = "Fedora" ]; then
		# Устанавливаем пакет с помощью пакетного менеджера dnf (rpm), если система - fedora
		sudo dnf install festvox-ru espeak espeak-ng rhvoice rhvoice-russian
	else
		# Сообщаем пользователю, что его система не поддерживается
		echo "Ваша операционная система ($distro) не поддерживается. Установите python-pip самостоятельно."
	fi
fi

# Устанавливаем зависимости (пакетный менеджер python3 - pip)
echo "Установка зависимостей (pip) . . . "
pip3 install -r requirements.txt											# Устанавливаем зависимости из файла req.txt
echo "Зависимости установлены (pip)!"

echo "Конфигурация голосового движка..."
cp .festivalrc -r ~/

# Сообщаем о завершении установки
echo "Установка завершена!"
