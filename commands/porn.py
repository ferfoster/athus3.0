import requests
import time
import json
import re
import os
from random import randint
import threading
import sys
import mimetypes
import requests
from bs4 import BeautifulSoup


class Porn(object):
    def __init__(self, file_name):
        self.session = requests.session()
        self.host = 'https://drrr.com/room/?ajax=1'
        self.spam = {"porn": False}
        self.file = open(file_name, 'r')
        self.session.cookies.update(eval(self.file.read()))
        self.file.close()

    def avoid_spam(self, com):
        time.sleep(5)
        self.spam[com] = False

    def post(self, message, url='', to=''):
        post_body = {
            'message': message,
            'url': url,
            'to': to
        }
        p = self.session.post(
            url=self.host, data=post_body)
        p.close()


    def gifporn(self, message, name_sender, id_sender):
        commandName = 'porn'
        if self.spam[commandName] == False:
            message = message[6:]
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 OPR/67.0.3575.137'}
            url =  "https://www.sex.com/search/gifs?query={}".format(message)
            conect = requests.get(url, headers=headers)
            soup = BeautifulSoup(conect.text, "lxml")
            porn_list = []
            cont  = 0
            try:
            	for i in range(0,15):
            		pornGif=soup.find_all('div',{'class':'masonry_box small_pin_box'})[i].find('img').get('data-src')
            		porn_list.append(pornGif)
            		cont += 1
            except Exception as e:
            	pass
            try:
            	maximo = len(porn_list)
            	x = randint(0, maximo)
            	print(porn_list[x])
            	self.post(message='{}'.format(message),
                      url='{}'.format(porn_list[x]), to=id_sender)
            	self.spam[commandName] = True
            	self.avoid_spam(commandName)
            except Exception as e:
            	pass





