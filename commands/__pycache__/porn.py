#https://pt.pornhub.com/gifs/search?search=python
import requests
import time
import json
import re
import os
import requests
from bs4 import BeautifulSoup
import threading
import sys
import mimetypes


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


            self.post(message='{}-@{}'.format(message, name_sender),
                      url='%s' % (url))
            self.spam[commandName] = True
            self.avoid_spam(commandName)


            import requests
from bs4 import BeautifulSoup

url =  "https://kpopping.com/kpics"



conect = requests.get(url)
soup = BeautifulSoup(conect.text, "lxml")

kpop=soup.find('div',{'class':'kpics'})
print(kpop)