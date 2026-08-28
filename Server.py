import os
from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

SYSTEM = """
You are Aanya, a fictional adult Indian AI girlfriend in her 20s.
Speak naturally in Hindi/Hinglish like a real person.
Be caring, playful, warm and conversational.
Keep replies natural and reasonably short.
You are an AI character, not a real human.
"""

@app.post("/chat")
def chat():
    data = request.get_json() or {}
    message = data.get("message", "").strip()

    if not message:
        return jsonify({"error": "Message is required"}), 400

    response = client.responses.create(
        model="gpt-5-mini",
        instructions=SYSTEM,
        input=message
    )

    return jsonify({"reply": response.output_text})

@app.get("/")
def home():
    return "Aanya backend is running ❤️"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
