import requests

print("Welcome to the Joke Bot!")
print("Type 'joke' to hear one, or 'quit' to exit.\n")

while True:
    user_input = input("You: ").lower()
    if user_input == "quit":
        print("Bot: Bye!")
        break
    elif user_input == "joke":
        try:
            response = requests.get("https://v2.jokeapi.dev/joke/Any?type=single")
            data = response.json()
            print("Bot: " + data["joke"])
        except:
            print("Bot: Couldn't fetch a joke right now.")
    else:
        print("Bot: Type 'joke' to get a laugh!")
