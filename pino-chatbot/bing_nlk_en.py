import random
import json
import datetime
import spacy
from bs import search_bing
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from nltk.chat.util import Chat, reflections

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

nlp_en = spacy.load("en_core_web_sm")
nlp_ko = spacy.load("ko_core_news_sm")
current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")

pairs = [
    ["hi", ["Hello!", "Hi there!"]],
    ["what is your name?", ["My name is Chatbot."]],
    ["bye", ["Goodbye!", "Bye!"]],
    ["what is the current date?", [f"The current date is {current_date}."]],
    ["what is an apple?", ["An apple is a round fruit with a red, green, or yellow skin and a white, juicy interior. It is a popular fruit and can be eaten raw or used in cooking and baking."]]
]

user_inputs = []


def get_doc(text):
    doc_en = nlp_en(text)
    doc_ko = nlp_ko(text)
    has_vector_norm = False
    for token in doc_en:
        if token.has_vector:
            has_vector_norm = True
            break
    if has_vector_norm and doc_en.vector_norm:
        return doc_en
    elif doc_ko.has_vector_norm and doc_ko.vector_norm:
        return doc_ko
    else:
        return None


def chatbot_response(user_input):
    bot_response = ""

    if user_input:
        doc = get_doc(user_input)

        if "time" in [token.text for token in doc] or "hour" in [token.text for token in doc]:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            bot_response = f"The current time is {current_time}."
        elif "date" in [token.text for token in doc]:
            current_date = datetime.datetime.now().strftime("%A, %B %d, %y")
            bot_response = f"The current date is {current_date}."
        else:
            # Example rule-based logic for generating response based on input
            chatbot = Chat(pairs, reflections)
            bot_response = chatbot.respond(user_input)

        if not bot_response:
            if user_input in data:
                if isinstance(data[user_input], list):
                    bot_response = random.choice(data[user_input])
                else:
                    bot_response = data[user_input]
            else:
                search_results = search_bing(user_input, num_results=3)
                if search_results:
                    bot_response = search_results[0]
                else:
                    bot_response = "I'm sorry, I'm not sure. Please try asking a different question or providing more information."

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
