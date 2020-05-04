import requests
import time
import json
import re,os
import threading
import sys
import mimetypes
import datetime


class admininstrator(object):
    def __init__(self, file_name):
        self.session = requests.session()
        self.host = 'https://drrr.com/room/?ajax=1'
        self.admin_list = ['kvh9Z.O9\/w', 'TqOzGmy5V.',
            'YJMpA.Wge2', 'NICKx2f4bE', 'vaW3kagV3.','A5w2NY1dws','hbX\/xjnbYc','.NEAR.hyA6']
        self.admin = ''
        self.banido = ''
        self.ban = True
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

    def setRomm_Description(self, message, tripcode):
        for i in range(len(self.admin_list)):
            if tripcode == self.admin_list[i]:
                message = message[11:]
                room_description_body = {'room_description': 'night {}'.format(message)}
                rd = self.session.post(self.host, room_description_body)
                rd.close()

    def setRomm_name(self, message, tripcode):
        for i in range(len(self.admin_list)):
            if tripcode == self.admin_list[i]:
                message = message[11:]
                room_name_body = {
                'room_name': message
                }
                rn = self.session.post(self.host, room_name_body)
                rn.close()

    def leave_room(self):
        leave_body = {
            'leave': 'leave'
        }
        lr = self.session.post(self.host, leave_body)
        lr.close()


    def new_host(self, new_host_id):
        new_host_body = {
            'new_host': new_host_id
        }
        nh = self.session.post(self.host, new_host_body)
        nh.close()

    def groom(self, new_host_id, tripcode):
        for i in range(len(self.admin_list)):
            if tripcode == self.admin_list[i]:
                new_host_body = {
                    'new_host': new_host_id
                }
                nh = self.session.post(self.host, new_host_body)
                nh.close()
        return True
        
    def admin_kick(self, message, name_sender, tripcode, id_sender):
        for i in range(len(self.admin_list)):
            if tripcode == self.admin_list[i]:
                if re.findall('/kick', message):
                    message = message[7:]

                    rooms = self.session.get(
                        "https://drrr.com/json.php?update=")
                    user = []
                    id_user = []

                    if rooms.status_code == 200:
                        rooms_data = json.loads(rooms.content)
                    for rooms in rooms_data['users']:
                        user.append(rooms)
                    for j in range(len(user)):
                        if user[j]['name'] == message:
                            kick_body = {'kick': user[j]['id']}
                            kc = self.session.post(
                                self.host, kick_body)
                            kc.close()
                            break

    def admin_ban(self, message, name_sender, tripcode, id_sender):
        self.ban = True
        for i in range(len(self.admin_list)):
            if tripcode == self.admin_list[i]:
                if re.findall('/ban', message):
                    message = message[6:]
                    rooms = self.session.get(
                        "https://drrr.com/json.php?update=")
                    user = []
                    id_user = []

                    if rooms.status_code == 200:
                        rooms_data = json.loads(rooms.content)
                    for rooms in rooms_data['users']:
                        user.append(rooms)
                    for j in range(len(user)):
                        if user[j]['name'] == message:
                            for a in range(len(self.admin_list)):
                                if user[j]['tripcode'] == self.admin_list[a]:
                                    self.ban = False
                                    self.post(message='Para de ser babacão', to=id_sender)
                            if self.ban == True:
                                ban_body = {'ban': user[j]['id']}
                                kc = self.session.post(
                                    self.host, ban_body)
                                kc.close()
                                self.admin = name_sender
                                self.banido = message
                                break


    def log(self):
        self.post(message='Ultimo Banimento:\n|ADM:{}|\n|Banido:{}|'.format(self.admin, self.banido))
