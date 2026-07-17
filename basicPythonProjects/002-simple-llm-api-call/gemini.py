from dotenv import load_dotenv
import requests
import os

load_dotenv()


class Gemini:
    def __init__(self):
        self.API_KEY = os.getenv("GEMINI_API_KEY")
        self.base_url = "https://generativelanguage.googleapis.com/v1/interactions"
        self.headers = {
            "x-goog-api-key": self.API_KEY,
            "Content-Type": "application/json",
        }
        self.previous_interaction_id = None

    def get_chat(self, chat):
        body = {
            "model": "gemini-3.5-flash",
            "input": chat,
            # "stream": True,
            "store": True,
        }
        # kalau previous_interaction_id sudah terisi
        if self.previous_interaction_id:
            body.update({"previous_interaction_id": self.previous_interaction_id})

        response = requests.post(self.base_url, headers=self.headers, json=body)
        response.raise_for_status()

        self.set_id(response.json()["id"])

        return response.json()

    # TODO: save to file
    def set_id(self, id):
        self.previous_interaction_id = id
