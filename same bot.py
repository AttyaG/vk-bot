import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import random
import time
import json

token = "40fcbd59d99133148cd4b53ab1e9ca0656ac84c5eb5165b1d16d57353aba18bb3c9800839191036b66a02"

vk = vk_api.VkApi(token=token)
vk._auth_token()

#data = json.load(open("keyboard.json"))

'''vk.method('messages.send',{"peer_id":id,
                                     "message":message},
                                     keyboard=open("keyboards.json", "r", encoding="UTF-8").read())
'''
"""def send_msg(self, id, message):
    Отправка сообщения через метод messages.send
    :param send_id: vk id пользователя, который получит сообщение
    :param message: содержимое отправляемого письма
    :return: None
    return self.vk.method('messages.send',{"peer_id":id,
                                     "message":message},
                                     keyboard=data)"""


commands = ["привет", "кто я?", "сыграем?"]
asks = ["Привет!", "ты хороший человек", "Да, только для начала...Давай познакомимся чуть получше! Ты же не против?"]


while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 40, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == commands[0]:
                #vk.method('photos.getMessagesUploadServer')["https://vk.com/k.attya?z=photo255100533_339416964%2Falbum255100533_0%2Frev"]
                vk.method("messages.send", {"peer_id": id, "message": asks[0], "random_id": random.randint(1, 2147483647)})
            elif body.lower() == commands[1]:
                vk.method("messages.send", {"peer_id": id, "message": asks[1], "random_id": random.randint(1, 2147483647)})
            elif body.lower() == commands[2]:
                vk.method("messages.send", {"peer_id": id, "message": asks[2], "random_id": random.randint(1, 2147483647)})
            else:
                vk.method("messages.send", {"peer_id": id, "message": "я не знаю что значит " + str(body.lower()), "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        time.sleep(1)


