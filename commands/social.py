import requests
import time
import json
import re
import os
from random import randint
import threading
import sys
import mimetypes


class Commands(object):
    def __init__(self, file_name):
        self.session = requests.session()
        self.host = 'https://drrr.com/room/?ajax=1'
        self.spam = {"gif": False, "help": False, "ship":False}
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

    def mensagemprivate(self, message, name_sender, to=''):
        if re.findall('/say .*', message):
           message = message[5:] #conta 5 carateres e depois imprime aquilo escrito
           self.post(message='%s' % (message)) #imprime a menssagem dita

    def help(self, message, name_sender):
        commandName = 'help'
        if self.spam[commandName] == False:
            try:
                self.post(
                    message="|==Comandos==|\n |/help|\n |/gif naruto|\n |/add music(ID)|\n|/play|\n|/skip|\n|/pause|\n|/queue|\n|/help music|\n |/pif gif pv|\n |/Porn (off)|")
                self.spam[commandName] = True
                self.avoid_spam(commandName)
            except Exception as e:
                print(e)

    def ghipy(self, message, name_sender, id_sender):
        commandName = 'gif'
        if self.spam[commandName] == False:
            message = message[5:]

            apikey = "LIVDSRZULELA"  # test value
            lmt = 8
            list_gif = []
            # our test search
            search_term = message

            r = requests.get(
                "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))
            if r.status_code == 200:
                top_8gifs = json.loads(r.content)
                maximo = len(top_8gifs['results']) - 1
                x = randint(0, maximo)
                list_gif.append(top_8gifs['results'][x])
                url = list_gif[0]['media'][0]['mediumgif']['url']
            self.post(message='{}-@{}'.format(message, name_sender),
                      url='%s' % (url))
            self.spam[commandName] = True
            self.avoid_spam(commandName)

    def gifid(self, message, name_sender, id_sender):
        commandName = 'gif'
        if self.spam[commandName] == False:
            message = message[5:]

            apikey = "LIVDSRZULELA"  # test value
            lmt = 8
            list_gif = []
            # our test search
            search_term = message

            r = requests.get(
                "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))
            if r.status_code == 200:
                top_8gifs = json.loads(r.content)
                maximo = len(top_8gifs['results']) - 1
                x = randint(0, maximo)
                list_gif.append(top_8gifs['results'][x])
                url = list_gif[0]['media'][0]['mediumgif']['url']
            self.post(message='{}'.format(message),
                      url='{}'.format(url), to=id_sender)
            self.spam[commandName] = True
            self.avoid_spam(commandName)


    def ship(self, message, name_sender):
        commandName = 'ship'
        if self.spam[commandName] == False:
            message = message[6:]
            x = randint(0, 10)
            ship = ""
            switcher = {
               0: "0%",
               1: "10%",
               2: "20%",
               3: "30%",
               4: "40%",
               5: "50%",
               6: "60%",
               7: "70%",
               8: "80%",
               9: "90%",
               10:"100%"
            }
            for i in range(0,x):
                ship += "█"
            total = switcher.get(x)
            self.post(message='|Shipmetro|\n{}\n{}{}'.format(message,ship,total))
            self.spam[commandName] = True
            self.avoid_spam(commandName)
