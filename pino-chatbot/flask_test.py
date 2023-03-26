import random
import json
import datetime
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from nltk.chat.util import Chat, reflections

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
current_time = datetime.datetime.now().strftime("%H:%M:%S")

pairs = [
    ["hi", ["Hello!", "Hi there!"]],
    ["what is your name?", ["My name is Chatbot."]],
    ["bye", ["Goodbye!", "Bye!"]],
    ["what is the current date?", [f"The current date is {current_date}."]],
    ["what is the current time?", [f"The current time is {current_time}."]],
]
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

user_inputs = []


def chatbot_response(user_input, confirm_message, new_data):
    bot_response = ""
    if user_input:
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

            if confirm_message:
                if confirm_message.lower() == "yes":
                    if new_data:
                        data[user_input] = new_data
                        with open("data.json", "w", encoding="utf-8") as f:
                            json.dump(data, f, ensure_ascii=False)
                        bot_response = (
                            "Thank you! I've added that to my knowledge base."
                        )
                    else:
                        bot_response = "I'm sorry, I didn't receive any new data. Please try again."
                else:
                    bot_response = "I'm sorry, I can't help with that."
            else:
                bot_response = "I'm not sure what you mean. Do you want to add this to my knowledge base?"

    else:
        save_user_input(user_input, bot_response)

    return bot_response


def save_user_input(user_input, bot_response):
    user_inputs.append({"user_input": user_input, "bot_response": bot_response})

    with open("user_inputs.json", "w", encoding="utf-8") as f:
        json.dump(user_inputs, f, ensure_ascii=False)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
@cross_origin()
def chat():
    user_input = request.form.get("user_input")
    confirm_message = request.form.get("confirm_message")
    new_data = request.form.get("new_data")
    bot_response = ""
    if user_input:
        bot_response = chatbot_response(user_input, confirm_message, new_data)
        response = {"bot_response": bot_response}
    else:
        response = {
            "bot_response": "I'm sorry, I did not receive any input. Please try again."
        }
    return response


if __name__ == "__main__":
    app.run(debug=True, port=8080)
