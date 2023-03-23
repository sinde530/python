import json
import random
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from nltk.chat.util import Chat, reflections

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

# load the chatbot data
pairs = [
    ["hi", ["Hello!", "Hi there!"]],
    ["what is your name?", ["My name is Chatbot."]],
    ["bye", ["Goodbye!", "Bye!"]],
]
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# define chatbot functions
user_inputs = []


def chatbot_response(user_input):
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

        if (
            "Please try asking a different question or providing more information."
            in bot_response
        ):
            confirm_message = "I don't have an answer for that. Can you tell me?"
            user_confirm = input(confirm_message)

            if user_confirm.lower() == "yes":
                try:
                    new_data = input("What's the answer to your question?")
                    data[user_input] = new_data
                    with open("data.json", "w", encoding="utf-8") as f:
                        json.dump(data, f, ensure_ascii=False)
                    bot_response = "Thank you! I've added that to my knowledge base."
                except Exception as e:
                    bot_response = "I'm sorry, there was an error processing your request: {}".format(
                        e
                    )
            else:
                bot_response = "I'm sorry, I can't help with that."

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
    bot_response = ""
    if user_input:
        bot_response = chatbot_response(user_input)
        response = {"bot_response": bot_response}
        print("else user_input", user_input)
        print("else bot_response", response)
    else:
        response = {
            "bot_response": "I'm sorry, I did not receive any input. Please try again."
        }
        print("else user_input", user_input)
        print("else bot_response", bot_response)
    return response


if __name__ == "__main__":
    app.run(debug=True, port=8080)
