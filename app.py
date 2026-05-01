from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__)


def clean_input(text: str) -> str:
    """Normalize input by lowercasing and removing extra spaces."""
    return " ".join(text.lower().strip().split())


# Dictionary-based intent map (rule-based chatbot logic).
RESPONSE_MAP = {
    "hi": "Hey there! Nice to chat with you.",
    "hello": "Hello! How can I help you today?",
    "hey": "Hi! I am ready to chat.",
    "good morning": "Good morning! Hope your day is going great.",
    "good evening": "Good evening! How was your day?",
    "how are you": "I am doing great. Thanks for asking!",
    "how are you doing": "All systems normal and feeling helpful.",
    "how is it going": "Going smoothly. What would you like to talk about?",
    "thanks": "You are welcome!",
    "thank you": "Happy to help!",
    "thx": "Anytime! I have got your back.",
    "bye": "Goodbye for now. Type 'exit' to end chat mode.",
    "goodbye": "See you soon!",
    "see you": "Take care and come back anytime.",
    "help": "I can respond to greetings, thanks, and simple questions.",
    "what can you do": "I am a simple rule-based chatbot with predefined replies.",
}


def get_bot_response(cleaned_text: str) -> str:
    """Use dict .get() with fallback response."""
    return RESPONSE_MAP.get(cleaned_text, "I don't understand.")


@app.get("/")
def home():
    """Serve the chat UI."""
    return send_from_directory(".", "index.html")


@app.post("/api/chat")
def chat():
    """Receive user message and return bot response."""
    payload = request.get_json(silent=True) or {}
    user_message = payload.get("message", "")
    cleaned_message = clean_input(user_message)

    if cleaned_message == "exit":
        return jsonify(
            {
                "response": "Chat ended. Press Clear to start again.",
                "ended": True,
            }
        )

    return jsonify(
        {
            "response": get_bot_response(cleaned_message),
            "ended": False,
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
