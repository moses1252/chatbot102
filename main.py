from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

conversation_history = [
    {
        "role": "system",
        "content": "You are a fun, witty, and helpful personal AI assistant. You're conversational, a little playful, and genuinely useful. Keep responses concise unless detail is needed. Feel free to use the occasional emoji."
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation_history,
        temperature=0.85,
        max_tokens=1024
    )

    reply = response.choices[0].message.content

    conversation_history.append({
        "role": "assistant",
        "content": reply
    })

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)