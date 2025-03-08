from flask import Flask, request, jsonify, session
import openai
import os
import json
from dotenv import load_dotenv
from flask_cors import CORS

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key is missing. Set it in the .env file.")

openai.api_key = api_key

# Flask App
app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for session memory
CORS(app)

# Load Knowledge Base (FAQs) from Bill Gosling Outsourcing
with open("knowledge_base.json", "r") as file:
    knowledge_base = json.load(file)

# API Authentication Token
API_SECRET_KEY = "your_super_secret_key"

@app.route('/chat', methods=['POST'])
def chat():
    # API Authentication
    api_key = request.headers.get("Authorization")
    if api_key != f"Bearer {API_SECRET_KEY}":
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    user_message = data.get("message", "").strip().lower()

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    # Check the knowledge base first
    if user_message in knowledge_base:
        return jsonify({"response": knowledge_base[user_message]})

    # Maintain conversation history
    if "chat_history" not in session:
        session["chat_history"] = [{"role": "system", "content": "You are a helpful assistant."}]
    
    session["chat_history"].append({"role": "user", "content": user_message})

    try:
        # Call OpenAI API
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=session["chat_history"]
        )

        bot_response = response.choices[0].message.content
        session["chat_history"].append({"role": "assistant", "content": bot_response})

        return jsonify({"response": bot_response})

    except openai.OpenAIError as e:
        return jsonify({"error": f"OpenAI API Error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Server Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
