import json
import nltk
from nltk.chat.util import Chat, reflections
import random

pairs = [
    ["hi", ["Hello!", "Hi there!"]],
    ["what is your name?", ["My name is Chatbot."]],
    ["bye", ["Goodbye!", "Bye!"]],
]

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Add more data
# data['What is the capital of France?'] = 'The capital of France is Paris.'
# data['한국어를 배우고 싶어요'] = ['한국어를 배우시려면 어떤 종류의 자료가 필요하신가요?', '한국어 배우기에 좋은 앱을 추천해드릴게요.']

try:
    with open("user_inputs.json", "r", encoding="utf-8") as f:
        user_inputs = json.load(f)
except FileNotFoundError:
    user_inputs = []


def save_user_input(user_input, bot_response):
    user_inputs.append({"user_input": user_input, "bot_response": bot_response})

    with open("user_inputs.json", "w", encoding="utf-8") as f:
        json.dump(user_inputs, f, ensure_ascii=False)


def chatbot_response(user_input):
    chatbot = Chat(pairs, reflections)
    bot_response = chatbot.respond(user_input)

    if bot_response:
        return bot_response

    if user_input in data:
        if isinstance(data[user_input], list):
            # bot_response = data[user_input][0]
            bot_response = random.choice(data[user_input])
        else:
            bot_response = data[user_input]
    else:
        bot_response = "I'm sorry, I'm not sure. Please try asking a different question or providing more information."

    if (
        "Please try asking a different question or providing more information."
        in bot_response
    ):
        confirm_message = "I don't have an answer for that. Can you tell me?"
        user_confirm = input(confirm_message)

        if user_confirm.lower() == "yes":
            new_data = input("What's the answer to your question?")
            data[user_input] = new_data
            with open("data.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False)

            bot_response = "Thank you! I've added that to my knowledge base."
        else:
            bot_response = "I'm sorry, I can't help with that."

    save_user_input(user_input, bot_response)

    return bot_response


while True:
    user_input = input("You: ")
    bot_response = chatbot_response(user_input)
    print("Bot:", bot_response)
