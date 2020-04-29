import requests
import time
import json
import re
import os
from random import randint 
import threading
import sys
import mimetypes
import datetime
global ts_last_greeting
ts_last_greeting = 0


class Module(object):
    def __init__(self, social, music, admin, configuration):
        self.session = requests.session()
        self.social = social
        self.music = music
        self.admin = admin
        self.configuration = configuration

    def load_cookie(self, file_name):
        f = open(file_name, 'r')
        self.session.cookies.update(eval(f.read()))
        f.close()

    def room_enter(self, url_room):
        re = self.session.get(url_room)
        re.close()
        room = self.session.get('https://drrr.com/json.php?fast=1')
        return room.text

    def room_update(self, room_text):
        update = re.search('"update":\d+.\d+', room_text).group(0)[9:]
        url_room_update = 'https://drrr.com/json.php?update=' + update
        while 1:
            time.sleep(1)
            ru = self.session.get(url_room_update)
            update = re.search('"update":\d+.\d+', ru.text).group(0)[9:]
            url_room_update = 'https://drrr.com/json.php?update=' + update

            if 'talks' in ru.text:
                talks_update = re.findall(
                    '{"id".*?"message":".*?"}', re.search('"talks":.*', ru.text).group(0))
                # talk in "talks" block
                for tu in talks_update:
                    info_sender = re.findall('"from":{.*?}', tu)
                    info_sender = info_sender[0]
                    try:
                        tripcode = re.findall(
                            '"tripcode":".*?"', info_sender)[0][12:-1]
                    except Exception:
                        tripcode = None
                    name_sender = re.findall(
                        '"name":".*?"', info_sender)[0][8:-1]
                    message = re.search('"message":".*?"', tu).group(0)[11:-1].encode(encoding='utf-8').decode(
                        encoding='unicode-escape')
                    # log mostrado no shell quando se execulta o bot
                    #print('@%s: %s' % (name_sender,message))
                    if '/' in message or '@Athus' in message:
                        info_sender = re.findall('"from":{.*?}', tu)
                        if info_sender:
                            info_sender = info_sender[0]
                            name_sender = re.findall(
                                '"name":".*?"', info_sender)[0][8:-1]
                            try:
                                tripcode = re.findall('"tripcode":".*?"', info_sender)[0][12:-1]
                            except Exception:
                                tripcode = None
                            # condição para o bot nao ficar auto se respondendo suas requisições
                            if name_sender == u'Athus':
                                continue
                            id_sender = re.findall(
                                '"id":".*?"', info_sender)[0][6:-1]
                            # pesquisa "to" no bloco html
                            info_receiver = re.findall('"to":{.*?}', tu)
                            # condição no main para verificar se o bot esta fora da sala/banido de alguma sala
                            if info_receiver:
                                is_leave = self.handle_private_message(message=message, id_sender=id_sender,
                                                                       name_sender=name_sender,tripcode=tripcode)
                                if is_leave:
                                    return True
                            else:
                                self.handle_message(message=message, name_sender=name_sender,
                                                    id_sender=id_sender)
            ru.close()

    def handle_message(self, message, name_sender, id_sender):
        if '/help' in message:
            t_help = threading.Thread(
                target=self.social.help, args=(message, name_sender))
            t_help.start()
        elif '/admin' in message:
            t_admin = threading.Thread(
                target=self.configuration.admin, args=(message, name_sender))
            t_admin.start()
        elif '/adm_list' in message:
            t_listAdmin = threading.Thread(
                target=self.configuration.listAdmin, args=(message, name_sender))
            t_listAdmin.start()
        elif '/gif' in message:
            t_ghipy = threading.Thread(
                target=self.social.ghipy, args=(message, name_sender, id_sender))
            t_ghipy.start()
        elif '/add' in message:
            t_music = threading.Thread(
                target=self.music.playlist, args=(message, name_sender, id_sender))
            t_music.start()
        elif '/play' in message:
            print('iniciando thread 1')
            t_play = threading.Thread(
                target=self.music.thPlay)
            t_play.start()
            print('saindo thread 1')
        elif '/pause' in message:
            t_pause = threading.Thread(
                target=self.music.pause_playlist)
            t_pause.start()
        elif '/skip' in message:
            t_skip = threading.Thread(
                target=self.music.skip_playlist)
            t_skip.start()
        elif '/queue' in message:
            t_next = threading.Thread(
                target=self.music.next)
            t_next.start()
        elif '/post_music' in message:
            t_music_help = threading.Thread(
                target=self.music.music_help, args=(message, name_sender))
            t_music_help.start()


    def handle_private_message(self, message, id_sender, name_sender, tripcode):
        if '/koi' in message:
            self.leave_room() # deixa a sala
            return True
        elif '/say' in message:
            t_mensagemprivate = threading.Thread(target=self.social.mensagemprivate, args=(message, name_sender, id_sender))
            t_mensagemprivate.start()
        elif '/add' in message:
            t_music = threading.Thread(
                target=self.music.playlist_anonimo, args=(message, name_sender,id_sender))
            t_music.start()
        elif '/groom' in message:
            self.admin.groom(new_host_id=id_sender)
        elif '/time_up' in message:
            self.configuration.Online()
        elif '/kloop' in message:
            t_loop = threading.Thread(target=self.configuration.loop_msg)
            t_loop.start()
        elif '/kick' in message:
            t_adm_k = threading.Thread(target=self.admin.admin_kick, args=(message, name_sender, tripcode, id_sender))
            t_adm_k.start()
        elif '/ban' in message:
            t_adm_ban = threading.Thread(target=self.admin.admin_ban, args=(message, name_sender, tripcode, id_sender))
            t_adm_ban.start()
        elif'/github' in message:
            self.configuration.merchan()
        elif'/room_name' in message:
            t_adm_name = threading.Thread(target=self.admin.setRomm_name, args=(message, tripcode))
            t_adm_name.start()
        elif'/room_info' in message:
            t_adm_description = threading.Thread(target=self.admin.setRomm_Description, args=(message, tripcode))
            t_adm_description.start()
        return False