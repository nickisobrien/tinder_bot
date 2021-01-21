import api
import time

from random import random

class Bot():
    def __init__(self, token, conv_starter):
        self.api = api.API(token)
        self.conv_starter = conv_starter

    def autolike(self, max_likes):
        max_sleep = 10
        print("Starting auotliking")

        while True:
            users = self.api.get_users()
            for user in users:
                if (max_likes <= 0):
                    print('Hit max likes')
                    return

                # Like the match
                res = self.api.like(user['user']['_id'])

                if (res['likes_remaining'] == 0):
                    print('Out of likes')
                    return
                max_likes-=1
                time.sleep(random() * max_sleep + 1)

    def auto_start_conversations(self):
        max_sleep = 10
        print("Starting automessaging")

        matches = self.api.get_matches()
        for match in matches:
            if (len(match['messages']) == 0):
                print(f"Sending message to {match['person']['name']}")
                self.api.send_message(match, match['id'], self.conv_starter)
                time.sleep(random() * max_sleep + 3)
