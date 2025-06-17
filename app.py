from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os

app = Flask(__name__)
CORS(app)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("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"))

@app.route("/gpt", methods=["POST"])
def gpt():
    data = request.get_json()
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        return jsonify({"response": response.choices[0].message.content.strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def index():
    return "UPAIBE is Live"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
