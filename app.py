# -*- coding:utf-8 -*-
# import athus
import os
import threading
import time
import json
import requests
from modules import module
from network import connect
from commands import social
from commands import music
from commands import admin
from commands import configuration



name = 'Athus'
icon = 'tanaka'
file_name = './cache/athus.cookie'
bot = connect.Connect(name=name, icon=icon)
if not os.path.isfile(file_name):
	bot.login()
	bot.save_cookie(file_name=file_name)
	music
configuration = configuration.Config(file_name=file_name)
admin = admin.admininstrator(file_name=file_name)
social = social.Commands(file_name=file_name)
music = music.musicSistem(file_name=file_name)
enter_room = module.Module(social=social ,music=music, admin=admin, configuration=configuration)
url_room = 'https://drrr.com/room/?id=27d90vxyqF'
# main
while True:
	try:
		enter_room.load_cookie(file_name=file_name)
		e_room = enter_room.room_enter(url_room=url_room)
		is_leave = enter_room.room_update(room_text=e_room)
		if is_leave == True:
			break
	except Exception as e:
		print(e)
