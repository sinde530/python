import json
import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ['hi', ['Hello!', 'Hi there!']],
    ['what is your name?', ['My name is Chatbot.']],
    ['bye', ['Goodbye!', 'Bye!']]
]

with open('data.json', 'r') as f:
    data = json.load(f)

try:
    with open('user_inputs.json', 'r') as f:
        user_inputs = json.load(f)
except FileNotFoundError:
    user_inputs = []


def save_user_input(user_input, bot_response):
    user_inputs.append(
        {'user_input': user_input, 'bot_response': bot_response})

    with open('user_inputs.json', 'w') as f:
        json.dump(user_inputs, f)


def chatbot_response(user_input):
    chatbot = Chat(pairs, reflections)
    bot_response = chatbot.respond(user_input)

    if bot_response:
        return bot_response

    if user_input in data:
        bot_response = data[user_input]
    else:
        bot_response = "I'm sorry, I'm not sure. Please try asking a different question or providing more information."

    if "Please try asking a different question or providing more information." in bot_response:
        # Check if the user input is a new question
        confirm_message = "I don't have an answer for that. Can you tell me?"
        user_confirm = input(confirm_message)

        if user_confirm.lower() == 'yes':
            new_data = input("What's the answer to your question? ")
            data[user_input] = new_data
            with open('data.json', 'w') as f:
                json.dump(data, f)

            bot_response = "Thank you! I've added that to my knowledge base."
        else:
            bot_response = "I'm sorry, I can't help with that."

    save_user_input(user_input, bot_response)

    return bot_response


while True:
    user_input = input('You: ')
    bot_response = chatbot_response(user_input)
    print('Bot:', bot_response)
