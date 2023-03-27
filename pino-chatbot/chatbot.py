import json
import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ["hi", ["Hello!", "Hi there!"]],
    ["what is your name?", ["My name is Chatbot."]],
    ["bye", ["Goodbye!", "Bye!"]],
]

# Load data from a JSON file
with open("data.json", "r") as f:
    data = json.load(f)

# Load user inputs from a JSON file
try:
    with open("user_inputs.json", "r") as f:
        user_inputs = json.load(f)
except FileNotFoundError:
    user_inputs = []


def save_user_input(user_input, bot_response):
    # Append the new user input to the list
    user_inputs.append(
        {"user_input": user_input, "bot_response": bot_response})

    # Write the updated list to the JSON file
    with open("user_inputs.json", "w") as f:
        json.dump(user_inputs, f)


def chatbot_response(user_input):
    # Use the Chat class from nltk to generate a response
    chatbot = Chat(pairs, reflections)
    bot_response = chatbot.respond(user_input)

    # If the response from the Chat class is not empty, return it
    if bot_response:
        return bot_response

    # Check if the user's input matches a key in the data file
    if user_input in data:
        bot_response = data[user_input]
    else:
        bot_response = "I'm sorry, I'm not sure. Please try asking a different question or providing more information."

    # Save the user input and bot response to the JSON file
    save_user_input(user_input, bot_response)

    # If the bot's response is a prompt, wait for the next user input
    if (
        "Please try asking a different question or providing more information."
        in bot_response
    ):
        return bot_response

    return bot_response


while True:
    user_input = input("You: ")
    bot_response = chatbot_response(user_input)
    print("Bot:", bot_response)
