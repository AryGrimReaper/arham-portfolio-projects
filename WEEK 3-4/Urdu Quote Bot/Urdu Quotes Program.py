import json
import random
import os

def load_quotes(category):
    filename = "quotes_" + category + ".json"
    if not os.path.exists(filename):
        print("Quote file not found for category:", category)
        return []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print("Error loading quotes:", e)
        return []

def get_random_quote(quotes):
    if not quotes:
        return None
    return random.choice(quotes)

def main():
    categories = {
        "1": "romantic",
        "2": "wisdom",
        "3": "life",
        "4": "exit"
    }

    # Pre-load all quotes
    quote_bank = {}
    for key in ["romantic", "wisdom", "life"]:
        quote_bank[key] = load_quotes(key)

    print("Urdu Quote Bot")
    while True:
        print("Choose a category:")
        print("1. Romantic Urdu Quotes")
        print("2. Wisdom Urdu Quotes")
        print("3. Life Urdu Quotes")
        print("4. Exit")
        choice = input("Enter 1, 2, 3 or 4: ").strip()

        if choice == "4":
            print("Goodbye.")
            break
        category = categories.get(choice)
        if not category:
            print("Invalid option. Please choose 1–4.")
            continue

        quote = get_random_quote(quote_bank[category])
        if quote:
            print("\nUrdu: " + quote["urdu"])
            print("Transliteration: " + quote["transliteration"])
            print("Translation: " + quote["translation"] + "\n")
        else:
            print("No quotes available in that category.\n")

if __name__ == "__main__":
    main()
