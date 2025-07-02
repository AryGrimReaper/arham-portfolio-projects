import time
import requests

reminders = []

def greet_user():
    name = input("Hi! I am THE Productivity Bot. What's your name? ")
    print("Nice to meet you, " + name + "! Let's Get you stay focused and get things done.")
    return name

def focus_timer():
    try:
        mins = int(input("How many minutes would you like to focus? "))
        print("Great! Starting your " + str(mins) + "-minute focus timer now. Stay focused Habibi!")
        time.sleep(2)  # Simulated time (for demo purposes)
        print("Time's up! You did great!")
    except ValueError:
        print("Please enter a valid number.")

def get_live_quote():
    print("Getting a motivational quote for you...")
    try:
        response = requests.get("https://zenquotes.io/api/random")
        if response.status_code == 200:
            data = response.json()
            quote = data[0]["q"]
            author = data[0]["a"]
            print("Quote: \"" + quote + "\" – " + author)
        else:
            print("Couldn't get a quote right now. Please try again later.")
    except:
        print("Oops! Something went wrong while getting the quote.")

def add_reminder():
    task = input("What would you like to be reminded about? ")
    reminders.append(task)
    print("Got it! I've added that to your list of reminders.")

def show_reminders():
    if not reminders:
        print("You don't have any reminders yet.")
    else:
        print("Here's what's on your reminder list:")
        count = 1
        for task in reminders:
            print(str(count) + ". " + task)
            count += 1

def main():
    name = greet_user()

    while True:
        print("What can I help you with today?")
        print("1. Set a focus timer")
        print("2. Get a motivational quote")
        print("3. Add a reminder")
        print("4. Show my reminders")
        print("5. Exit")

        choice = input("Enter a number or type a command: ").strip().lower()

        if choice in ["1", "focus", "timer"]:
            focus_timer()
        elif choice in ["2", "quote", "motivate"]:
            get_live_quote()
        elif choice in ["3", "reminder", "add"]:
            add_reminder()
        elif choice in ["4", "show", "reminders"]:
            show_reminders()
        elif choice in ["5", "exit", "bye"]:
            print("Goodbye " + name + "! Keep up the great work!")
            break
        else:
            print("Hmm, I didn't get that. Please try choosing from the list.")

if __name__ == "__main__":
    main()
