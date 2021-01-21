import requests

from random import random

TINDER_URL = "https://api.gotinder.com"

class API():

    def __init__(self, token):
        self.token = token

    def like(self, match_id):
        res = requests.post(TINDER_URL + f"/like/{match_id}", headers={"x-auth-token": self.token}).json()
        return {
            "is_match": res["match"],
            "likes_remaining": res["likes_remaining"]
        }

    def dislike(self, match_id):
        res = requests.get(TINDER_URL + f"/v2/pass/{match_id}?locale=en",
            headers = {"x-auth-token": self.token}).json()

    def get_matches(self):
        res = requests.get(TINDER_URL + f"/v2/matches?locale=en&count=60",
            headers = {"x-auth-token": self.token}).json()
        return(res["data"]["matches"]);

    def get_users(self):
        res = requests.get(TINDER_URL + "/v2/recs/core?locale=en",
            headers = {"x-auth-token": self.token}).json()
        return(res["data"]["results"])

    def send_message(self, match_id, message):
        res = requests.post(TINDER_URL + f"/user/matches/{match_id}?locale=en",
            headers = {"x-auth-token": self.token},
            data = { "message": message})
