import requests
import time
import json
import sys
import mimetypes
import datetime


class Config(object):
    def __init__(self, file_name):
        self.session = requests.session()
        self.host = 'https://drrr.com/room/?ajax=1'
        self.start_time = datetime.datetime.utcnow()
        self.admin_list = ['TqOzGmy5V.','A5w2NY1dws']
        self.spam = {"admin_list": False,"admin": False}
        self.loop = True
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
    #private
    def merchan(self):
        mercham = "https://github.com/londarks"
        self.post(message="Olá Meu nome e Athus e eu fui Criado por Londarks\n Caso queira saber como fui feito segue o link abaixo", url='{}'.format
                  (mercham))  # de

    def admin(self, message, name_sender):
        commandName = 'admin'
        if self.spam[commandName] == False:
            self.post(
                message="|==ADMIN==|\n |/adm_list| \n |/kick name|\n |/ban name|\n |/room_name Name_room|\n |/room_info Description|\n |/host|")
            self.spam[commandName] = True
            self.avoid_spam(commandName)

    def listAdmin(self, message, name_sender):
        commandName = 'admin_list'
        if self.spam[commandName] == False:
            self.post(
                message="|==ADMIN's==| \n |@londarks|\n |@NICK!|\n |@alim|\n |@MECK!|\n |@jenni|\n |@NEKO|\n |@100sentido|")
            self.spam[commandName] = True
            self.avoid_spam(commandName)

#private menssagem
    def loop_msg(self, tripcode, id_sender):
        for i in range(len(self.admin_list)):
            if tripcode == self.admin_list[i]:
                if self.loop == True:
                    self.loop = False
                    while 1:
                        time.sleep(600)
                        print("loop pegando")
                        now = datetime.datetime.utcnow()  # Timestamp of when uptime function is run
                        delta = now - self.start_time
                        hours, remainder = divmod(int(delta.total_seconds()), 3600)
                        minutes, seconds = divmod(remainder, 60)
                        days, hours = divmod(hours, 24)
                        if days:
                            time_format = "{d}days,{h}hours,{m}minutes,{s}seconds."
                        else:
                            time_format = "{d}days,{h}hours,{m}minutes,{s}seconds."
                        uptime_stamp = time_format.format(
                            d=days, h=hours, m=minutes, s=seconds)
                        self.post(message='/me Time Online:{}'.format(uptime_stamp))
                else:
                    self.post(message='Comando Ja em inicialização', to=id_sender)