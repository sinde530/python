import random
import json
import datetime
from bs import search_bing
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from nltk.chat.util import Chat, reflections
import re

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")

pairs = [
    ["hi", ["Hello!", "Hi there!"]],
    ["what is your name?", ["My name is Chatbot."]],
    ["bye", ["Goodbye!", "Bye!"]],
    ["what is the current date?", [f"The current date is {current_date}."]],
    ["what is an apple?", ["An apple is a round fruit with a red, green, or yellow skin and a white, juicy interior. It is a popular fruit and can be eaten raw or used in cooking and baking."]]
]

user_inputs = []


def chatbot_response(user_input):
    bot_response = ""
    if user_input:
        if re.search(r"\b(time|what.*hour)\b", user_input, re.IGNORECASE):
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            bot_response = f"The current time is {current_time}."
        elif re.search(r"\b(date|what.*date)\b", user_input, re.IGNORECASE):
            current_date = datetime.datetime.now().strftime("%A, %B %d, %y")
            bot_response = f"The current date is {current_date}."
        else:
            chatbot = Chat(pairs, reflections)
            bot_response = chatbot.respond(user_input)

        if not bot_response:
            if user_input in data:
                if isinstance(data[user_input], list):
                    bot_response = random.choice(data[user_input])
                else:
                    bot_response = data[user_input]
            else:
                bot_response = "I'm sorry, I'm not sure. Please try asking a different question or providing more information."

                search_results = search_bing(user_input, num_results=3)
                if search_results:
                    bot_response += "\n\nHere are some links that might help:\n"
                    for result in search_results:
                        bot_response += f"\n- {result}"

                bot_response += "\n\nWould you like me to add this to my knowledge base?"

        else:
            save_user_input(user_input, bot_response)

    else:
        bot_response = "I'm sorry, I did not receive any input. Please try again."

    return bot_response


def save_user_input(user_input, bot_response):
    user_inputs.append(
        {"user_input": user_input, "bot_response": bot_response})

    with open("user_inputs.json", "w", encoding="utf-8") as f:
        json.dump(user_inputs, f, ensure_ascii=False)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
@cross_origin()
def chat():
    user_input = request.form.get("user_input")
    bot_response = ""
    if user_input:
        bot_response = chatbot_response(user_input)
        response = {"bot_response": bot_response}
    else:
        response = {
            "bot_response": "I'm sorry, I did not receive any input. Please try again."
        }
    return response


if __name__ == "__main__":
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    app.run(debug=True, port=8080)
