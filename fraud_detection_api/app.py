
# app.py

from flask import Flask, request, jsonify
import joblib
from cleaner import clean_text_mixed_with_stopwords
from flask_cors import CORS
app = Flask(__name__)
CORS(app)  # Allow cross-origin requests


# Initialize Flask app
app = Flask(__name__)

# Load the model and vectorizer
model = joblib.load("fraud_model_lr.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Get message
    message = data.get("message", "")
    if not message:
        return jsonify({"error": "No message provided"}), 400

    # Clean the message
    cleaned = clean_text_mixed_with_stopwords(message)
    vector = vectorizer.transform([cleaned])
    prediction = model.predict(vector)[0]

    result = "🚨 Scam" if prediction == 1 else "✅ Legit"
    return jsonify({
        "message": message,
        "cleaned": cleaned,
        "prediction": result,
        "label": int(prediction)
    })

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

