from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import nltk
from nltk.tokenize import word_tokenize
import re
import string

# Download punkt tokenizer if not already downloaded

#nltk.download("punkt")


app = Flask(__name__)
CORS(app)

# Load the trained model
model = joblib.load("fraud_model_lr.pkl")

# Text cleaning function
# 🔁 Modified clean_text for production use:
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s\u0900-\u097F]", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = text.split()  # No NLTK needed
    return " ".join(tokens)


# ✅ Home route with usage instructions
@app.route("/", methods=["GET"])
def home():
    return """
    <h2>🚨 Cyber Fraud Detection API</h2>
    <p>Welcome to the Fraud Alert Assistant API.</p>
    <p><strong>POST</strong> your suspicious message to <code>/predict</code> as JSON like:</p>
    <pre>{
  "message": "आपका PAN कार्ड ब्लॉक कर दिया गया है।"
}</pre>
    <p>You'll receive a JSON response with prediction: <code>'🚨 Scam'</code> or <code>'✅ Legit'</code></p>
    <p>Made by Akash Sare 💡</p>
    """

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    message = data.get("message", "")
    cleaned = clean_text(message)
    prediction = model.predict([cleaned])[0]
    label = "🚨 Scam" if prediction == 1 else "✅ Legit"

    return jsonify({
        "message": message,
        "cleaned": cleaned,
        "prediction": label,
        "label": int(prediction)
    })

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
