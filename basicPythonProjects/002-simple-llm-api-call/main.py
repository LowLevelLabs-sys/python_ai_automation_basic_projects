from dotenv import load_dotenv
import requests
import os

base_url = "https://generativelanguage.googleapis.com/v1/interactions"
API_KEY = os.getenv("GEMINI_API_KEY")
headers = {"x-goog-api-key": API_KEY, "Content-Type": "application/json"}


def get_chat(chat):
    body = {"model": "gemini-3.5-flash", "input": chat}

    response = requests.post(base_url, headers=headers, json=body)
    response.raise_for_status()

    return response.json()


def main():
    chat = input("> ")

    response = get_chat(chat)

    # text = response["steps"][0] == ["type": "thought", "signature": "blablabla"]
    text = response["steps"][1]["content"][0]["text"]

    print(text)


if __name__ == "__main__":
    main()
