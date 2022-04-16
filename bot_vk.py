import random
import vk_api
from datetime import datetime
from vk_api.longpoll import VkLongPoll, VkEventType

token = ""
vk_session = vk_api.VkApi(token=token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
def send_message(vk_session, id_type, id, message=None, attachment=None):
    vk_session.method('messages.send',{id_type: id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648), "attachment": attachment})
while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print('Текст сообщения: ' + str(event.text))
            print('id' + str(event.peer_id))
            print()
            response = event.text.lower()
            if event.from_user and not (event.from_me):
                if response == "111111111111111":
                    vk_session.method('messages.send', {'peer_id': event.peer_id, 'message':'Драсти!', 'random_id': 0})
                elif response == "тест":
                    vk_session.method('messages.send', {'peer_id': event.peer_id, 'message': 'работает', 'random_id': 0})
                else:
                	vk_session.method("messages.send", {'peer_id': event.peer_id, 'message': 'В данный момент бот отключён!,приносим свои извинения.','random_id': 0})		