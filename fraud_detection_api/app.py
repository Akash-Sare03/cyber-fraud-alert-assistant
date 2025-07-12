from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import nltk
from cleaner import clean_text_mixed_with_stopwords

nltk.data.path.append("./nltk_data")


app = Flask(__name__)
CORS(app)

# Load the saved ML model and vectorizer
model = joblib.load("fraud_model_lr_new.pkl")
vectorizer = joblib.load("tfidf_vectorizer_new.pkl")

# Home route for testing
@app.route("/", methods=["GET"])
def home():
    return """
    <h2>🚨 Cyber Fraud Detection API</h2>
    <p>Send a POST request to <code>/predict</code> with your message:</p>
    <pre>{ "message": "आपका अकाउंट बंद हो गया है..." }</pre>
    """

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    message = data.get("message", "")

    # Step 1: Clean the message
    cleaned = clean_text_mixed_with_stopwords(message)

    # Step 2: Vectorize
    vector_input = vectorizer.transform([cleaned])

    # Step 3: Predict using ML model
    prediction = model.predict(vector_input)[0]
    label = "🚨 Scam" if prediction == 1 else "✅ Legit"

    # Step 4: Smart Boosting - Rule-based override
    scam_keywords = [
        "खाता", "ब्लॉक", "suspended", "बंद", "ACCOUNT BLOCK UPDATE KYC", "SHARE OTP", "link", "click", "संपर्क", "suspicious", "जीते"
    ]
    safe_patterns = [
        "otp है", "otp:", "your otp", "पैमेंट सफल", "बिल सफल", "बुकिंग", "कन्फर्म", "सफलतापूर्वक"
    ]
    cleaned_lower = cleaned.lower()

    if prediction == 0:  # If model says Legit
        if any(word in cleaned_lower for word in scam_keywords):
            if not any(pattern in cleaned_lower for pattern in safe_patterns):
                label = "🚨 Scam (flagged by rule)"

    return jsonify({
        "message": message,
        "cleaned": cleaned,
        "result": label
    })

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
