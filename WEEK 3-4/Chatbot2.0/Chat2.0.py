from textblob import TextBlob
import datetime

def detect_mood_by_keywords(text):
    text = text.lower()
    if "happy" in text or "excited" in text:
        return "happy"
    elif "sad" in text or "depressed" in text or "unhappy" in text:
        return "sad"
    elif "tired" in text or "sleepy" in text:
        return "tired"
    elif "bored" in text:
        return "bored"
    elif "angry" in text or "mad" in text:
        return "angry"
    else:
        return "unknown"

def detect_mood_by_sentiment(text):
    sentiment_score = TextBlob(text).sentiment.polarity
    if sentiment_score > 0.3:
        return "happy"
    elif sentiment_score < -0.3:
        return "sad"
    else:
        return "neutral"

def generate_response(mood):
    responses = {
        "happy": "That's great to hear! Keep enjoying your day!",
        "sad": "I'm here for you. Maybe talk to a friend or get some fresh air.",
        "tired": "Make sure to rest and hydrate. You deserve a break.",
        "bored": "Try starting a small project or watching something inspiring.",
        "angry": "Take a few deep breaths. Writing your thoughts down might help.",
        "neutral": "Thanks for sharing. Let me know if there's anything I can do.",
        "unknown": "I'm not sure how you're feeling, but I'm here to chat!"
    }
    return responses.get(mood, responses["unknown"])

def save_chat(name, mood, user_input):
    try:
        with open("chat_log.txt", "a") as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp} - {name} ({mood}): {user_input}\n")
        print("Chat saved to 'chat_log.txt'.")
    except Exception as e:
        print("Error saving chat:", e)

def run_chatbot():
    print("Welcome to MoodBot Pro!")
    name = input("What's your name? ")

    user_input = input("Hi " + name + ", how are you feeling today? Describe in one or two sentences:\n")

    # Dual detection: sentiment + keywords
    mood_by_keywords = detect_mood_by_keywords(user_input)
    mood_by_sentiment = detect_mood_by_sentiment(user_input)

    # Priority: sentiment detection unless it's "neutral"
    mood = mood_by_sentiment if mood_by_sentiment != "neutral" else mood_by_keywords

    response = generate_response(mood)
    print(f"\nMoodBot: {response}")

    save = input("\nWould you like to save this conversation? (yes/no): ").strip().lower()
    if save == "yes":
        save_chat(name, mood, user_input)
    else:
        print("Session ended without saving.")

# Run the chatbot
run_chatbot()
