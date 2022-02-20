import random
import time
import requests
import json

from app.user import User


class Client:
    HEADERS = {'Content-Type': 'application/json'}

    def __init__(self, url):
        self._event_id = 0
        self._url = url

    def run(self):
        user_list = []
        while True:
            self._event_id += 1
            uid = random.randint(0, len(user_list)) + 1
            if uid == len(user_list) + 1:
                currency = random.choice(['krw', 'usd'])
                user = User(uid, currency)
                user_list.append(user)
            else:
                user = user_list[uid-1]

            user.act()
            message = self.to_message(user)
            print(message)
            requests.post(self._url, data=json.dumps(message), headers=Client.HEADERS)

            time.sleep(0.5)

    def to_message(self, user):
        message = dict()
        message['event_id'] = self._event_id
        message['user_id'] = user.get_id()
        message['event'] = user.get_state()
        message['parameters'] = user.get_param()
        return message
