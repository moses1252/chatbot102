# Chatbot102 🤖

A personal AI assistant built with Python, Flask, and OpenAI. Runs locally in your browser — no API key ever exposed to the frontend.

## Tech Stack

- **Python** — backend language
- **Flask** — lightweight web server that handles requests between the browser and OpenAI
- **OpenAI API** — powers the AI responses (uses `gpt-4o-mini`)
- **python-dotenv** — loads your secret API key from a `.env` file safely
- **uv** — modern Python package manager used to install dependencies

## Project Structure

```
chatbot102/
├── .env               ← your secret API key (never uploaded to GitHub)
├── .gitignore         ← tells Git to ignore .env and other junk files
├── main.py            ← Flask server that talks to OpenAI
├── pyproject.toml     ← project dependencies managed by uv
├── README.md          ← this file
└── templates/
    └── index.html     ← the chat UI that loads in your browser
```

## Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/chatbot102.git
cd chatbot102
```

### 2. Install dependencies
```bash
uv sync
```

### 3. Create your `.env` file
Create a file called `.env` in the root of the project and add your OpenAI API key:
```
OPENAI_API_KEY=sk-yourrealkeyhere
```
> ⚠️ Never share this file or commit it to GitHub. It's already in `.gitignore` to protect you.

### 4. Run the app
```bash
uv run main.py
```

### 5. Open in your browser
Go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

## How It Works

1. You type a message in the browser
2. The frontend sends it to Flask (`/chat` endpoint)
3. Flask forwards it to OpenAI using your secret API key
4. OpenAI replies and Flask sends it back to the browser
5. Your API key never touches the frontend ✅

## Getting an OpenAI API Key

1. Go to [https://platform.openai.com](https://platform.openai.com)
2. Sign up or log in
3. Go to **API Keys** and create a new key
4. Paste it into your `.env` file