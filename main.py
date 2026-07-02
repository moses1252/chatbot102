from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

##this calls apis im guessing
app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

##this is a friendly message to user saved as an array of some sort
conversation_history = [
    {
        "role": "system",
        "content": "You are a fun, witty, and helpful personal AI assistant. You're conversational, a little playful, and genuinely useful. Keep responses concise unless detail is needed. Feel free to use the occasional emoji."
    }
]

##this is a pointer to where they look for the correct file
@app.route("/")
def index():
    return render_template("index.html")

##this takes your data and sends it to the url/database
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    ##guessing this catches an error and lets program continue
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    ##add user message to array so we have memory for the api
    ##because it doesn't remember the chat everytime we send a message
    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    ##variable to save api response and api response
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation_history,
        temperature=0.85,
        max_tokens=1024
    )

    #get first item in reponse arr
    #which i think is the api chatbot reply
    reply = response.choices[0].message.content

    #put api call in convo history variable to keep track of api chatbot response too
    conversation_history.append({
        "role": "assistant",
        "content": reply
    })

    #give the api chatbot reply to whoever called this function
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)