# === File: app.py ===
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
import requests
from utils import generate_followup_email, generate_report, generate_onboarding_quiz, simulate_lead_scrape

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/gpt", methods=["POST"])
def gpt():
    data = request.get_json()
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are a business improvement assistant."},
                     {"role": "user", "content": prompt}]
        )
        return jsonify({"response": response.choices[0].message['content'].strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/leads/live", methods=["POST"])
def lead_scraper():
    data = request.get_json()
    return jsonify({"leads": simulate_lead_scrape(data.get("industry", ""), data.get("location", ""))})

@app.route("/report", methods=["POST"])
def report_generator():
    data = request.get_json()
    return jsonify({"report": generate_report(data.get("focus", "monthly performance"))})

@app.route("/email/followup", methods=["POST"])
def followup_email():
    data = request.get_json()
    lead_info = data.get("lead", {})
    if not lead_info:
        return jsonify({"error": "Missing lead information"}), 400
    return jsonify({"email": generate_followup_email(lead_info)})

@app.route("/crm/handoff", methods=["POST"])
def crm_handoff():
    data = request.get_json()
    sheet_url = os.getenv("GOOGLE_SHEET_WEBHOOK")
    if not sheet_url:
        return jsonify({"error": "No webhook URL configured."}), 500

    try:
        r = requests.post(sheet_url, json=data)
        return jsonify({"status": "sent to Google Sheets", "response": r.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/onboarding/quiz", methods=["POST"])
def onboarding_quiz():
    data = request.get_json()
    industry = data.get("industry", "general")
    return jsonify({"questions": generate_onboarding_quiz(industry)})

@app.route("/")
def index():
    return "UPAIBE system is active."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
