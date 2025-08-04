import os
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Sample data for demonstration
sample_data = {
    "today_usage": 120,
    "weekly_trend": [90, 110, 130, 100, 120, 140, 150],
    "app_usage": [
        {"name": "Instagram", "minutes": 60},
        {"name": "YouTube", "minutes": 40},
        {"name": "Twitter", "minutes": 20}
    ],
    "alerts": ["You exceeded your daily limit on Instagram!"]
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/dashboard")
def dashboard():
    return jsonify(sample_data)

@app.route("/api/save-settings", methods=["POST"])
def save_settings():
    data = request.json
    # In real app, save to database
    return jsonify({"status": "success", "message": "Settings saved"})

@app.route("/api/start-challenge", methods=["POST"])
def start_challenge():
    data = request.json
    challenge_type = data.get("type")
    return jsonify({
        "status": "success", 
        "message": f"{challenge_type} challenge started!"
    })

@app.route("/api/save-reflection", methods=["POST"])
def save_reflection():
    data = request.json
    reflection = data.get("reflection")
    # In real app, save to database
    return jsonify({"status": "success", "message": "Reflection saved"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
