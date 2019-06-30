import vk_api
import random
import time
import json

token = "ваш токен"

vk = vk_api.VkApi(token=token)
vk._auth_token()

commands = ["привет", "кто я?", "сыграем?"]
asks = ["Привет!", "ты хороший человек", "Да, только для начала...Давай познакомимся чуть получше! Ты же не против?"]

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 40, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == commands[0]:
                vk.method("messages.send", {"peer_id": id, "message": asks[0], "random_id": random.randint(1, 2147483647)})
            elif body.lower() == commands[1]:
                vk.method("messages.send", {"peer_id": id, "message": asks[1], "random_id": random.randint(1, 2147483647)})
            elif body.lower() == commands[2]:
                vk.method("messages.send", {"peer_id": id, "message": asks[2], "random_id": random.randint(1, 2147483647)})
            else:
                vk.method("messages.send", {"peer_id": id, "message": "я не знаю что значит " + str(body.lower()), "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        time.sleep(1)


