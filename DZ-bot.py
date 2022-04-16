import sys
import math
import time
import vk_api
import random
from datetime import datetime
from vk_api.longpoll import VkLongPoll, VkEventType
#--------------------переменные----------------------------

#--------------------переменные----------------------------
token = ""
vk_session = vk_api.VkApi(token=token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
print("Бот запущен!")
def send_message(vk_session, id_type, id, message=None, attachment=None):
    vk_session.method('messages.send',{id_type: id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648), "attachment": attachment})
while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M")))
            print('Текст сообщения: ' + str(event.text))
            response = event.text.lower()
            if event.from_user and not (event.from_me):
                if response == "дз" or response == "д" or response == "домашка":
                    vk_session.method('messages.send', {'peer_id': event.peer_id, 'message':(pn),'random_id': 0})
                elif response == "/*/*/*/*/*/*/":
                    vk_session.method('messages.send', {'peer_id': event.peer_id, 'message':'3', 'random_id': 0})
                    vk_session.method('messages.send', {'peer_id': event.peer_id, 'message':'2', 'random_id': 0})
                    vk_session.method('messages.send', {'peer_id': event.peer_id, 'message':'1', 'random_id': 0})
                    vk_session.method('messages.send', {'peer_id': event.peer_id, 'message':'Выключение✅', 'random_id': 0})
                    vk_session.method('messages.send', {'peer_id': event.peer_id, 'message':'++'+str(vk), 'random_id': 0})
                elif response == "номерки" or response == "номера":
                    vk_session.method('messages.send', {'peer_id': event.peer_id, 'message':"""Номер|          Ф И О""", 'random_id': 0})
                elif response == "нд":
                    vk_session.method('messages.send', {'peer_id': event.peer_id, 'message':'📌НЕ ДОБАВЛЕННЫЕ В ГРУППУ\n', 'random_id': 0})
                elif response == "помощь":
                    vk_session.method('messages.send', {'peer_id': event.peer_id, 'message':'КОМАНДЫ БОТА:\n📚дз-[домашнее задание]\n♦️нд-[не добавленные в группу]\n📋номера-[номера в раздевалке]\n🚍автобусы-[расписание автобусов]', 'random_id': 0})
                elif response == "автобусы":
                    vk_session.method('messages.send', {'peer_id': event.peer_id, 'message':'🚍Расписание автобусов: \n', 'random_id': 0})    
                else:
                    vk_session.method("messages.send", {'peer_id': event.peer_id, 'message': 'Команда не распознана!','random_id': 0})