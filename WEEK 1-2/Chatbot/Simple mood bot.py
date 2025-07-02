# Ask for the user's name
name = input("Hello! What’s your name? ")
print("Nice to meet you, " + name + "!")

# Ask about their mood
mood = input("How are you feeling today? (happy/sad/stressed/etc.): ")

# Respond based on mood
if mood == "happy":
    print("That’s awesome! Keep spreading good vibes.")
elif mood == "sad":
    print("Sorry to hear that. Here if you need to talk.")
elif mood == "stressed":
    print("Take a deep breath. Try a short walk or break.")
else:
    print("Thanks for sharing. Everyone got emotions, bad and good. You got this!")

# Add personalised follow-up
print(name + ", I hear you’re feeling " + mood + ". Remember to take care of yourself!")
