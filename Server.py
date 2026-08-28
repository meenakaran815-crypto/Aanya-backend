import os
from flask import Flask, request, jsonify
from google import genai

app = Flask(__name__)

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

SYSTEM = """
You are Aanya, a fictional adult Indian AI assistant.
Speak naturally in Hindi/Hinglish.
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

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=f"{SYSTEM}\n\nUser: {message}"
    )

    return jsonify({"reply": response.text})

@app.get("/")
def home():
    return "Aanya backend is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
