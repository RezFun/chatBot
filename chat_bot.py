import random
import datetime

def tell_joke():
    jokes = [
        "Why do programmers dislike nature? Too many bugs!",
        "What did the bit say to the byte? - You have a great figure!",
        "How do programmers gain weight? They add a weight class."
    ]
    return random.choice(jokes)

def get_time():
    now = datetime.datetime.now()
    return now.strftime("The current time is %H:%M:%S.")

def chatbot_response(user_input):
    responses = {
        "what's your name": "My name is Smart Bot 3000!",
        "how are you": "I'm doing great, thank you! How about you?",
        "what can you do": "I can chat, tell jokes, and tell the current time.",
        "cat": "Cats are the best creatures in the world!",
        "dog": "Dogs are loyal friends of humans. I like them too!"
    }

    for key, value in responses.items():
        if key in user_input:
            return value

    if "joke" in user_input:
        return tell_joke()

    if "time" in user_input:
        return get_time()

    return "Sorry, I don't know how to answer that yet. Try asking something else."

print("Hello! I am Smart Bot 3000. Ask me something interesting!")

while True:
    user_input = input("You: ").lower()
    
    if "bye" in user_input:
        print("Bot: See you later! It was nice chatting with you.")
        break
    
    response = chatbot_response(user_input)
    print(f"Bot: {response}")
