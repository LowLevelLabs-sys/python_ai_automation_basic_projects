from gemini import Gemini

gemini = Gemini()


def main():
    while True:
        chat = input("> ")

        response = gemini.get_chat(chat)

        # text = response["steps"][0] == ["type": "thought", "signature": "blablabla"]
        text = response["steps"][1]["content"][0]["text"]
        print(text)

        if input("exit (y/n):") == "y":
            print("bye~!")
            break


if __name__ == "__main__":
    main()
