from dotenv import load_dotenv
import requests
import os
import json

load_dotenv()


class Gemini:
    def __init__(self):
        self.API_KEY = os.getenv("GEMINI_API_KEY")
        self.base_url = "https://generativelanguage.googleapis.com/v1/interactions"
        self.headers = {
            "x-goog-api-key": self.API_KEY,
            "Content-Type": "application/json",
        }

        self.previous_interaction_id = self.read_previous_id()

    def get_chat(self, chat):
        body = {
            "model": "gemini-3.5-flash",
            "input": chat,
            # "stream": True,
            "store": True,
        }

        # if the previous_interaction_id exist and not none
        if self.previous_interaction_id is not None:
            body.update({"previous_interaction_id": self.previous_interaction_id})

        response = requests.post(self.base_url, headers=self.headers, json=body)
        response.raise_for_status()

        self.previous_interaction_id = response.json()["id"]
        self.save_previous_id(response.json()["id"])

        return response.json()

    def read_previous_id(self):
        try:
            with open("previous_interaction_id.json", "r") as target:
                data = json.load(target)
                return data["previous_interaction_id"]
        except FileNotFoundError:
            return None

    def save_previous_id(self, id):
        with open("previous_interaction_id.json", "w") as target:
            json.dump({"previous_interaction_id": id}, target)
