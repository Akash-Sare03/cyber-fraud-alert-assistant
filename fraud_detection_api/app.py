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
        "खाता", "ब्लॉक", "suspended", "बंद", "ACCOUNT BLOCK UPDATE KYC", "SHARE OTP", "link", "click", "संपर्क",
        "suspicious", "जीते", "Rummy", "Bonus" , "free gift" , "dream11",
    "my11circle",
    "fantasy cricket",
    "get ₹", "win ₹", "won ₹", "claim ₹",
    "lottery", "lucky draw", "you have won",
    "kyc update", "kyc suspended", "sim block",
    "click link", "verify now", "update now",
    "urgent", "final notice", "your account will be suspended",
    "your sbi account", "your bank account",
    "blocked due to inactivity", "verify to avoid suspension",
    "click below", "job offer", "income from home",
    "government scheme", "pm yojana", "loan approved",
    "instant loan", "zero interest", "free recharge",
    "upi id not active", "upi suspended",
    "whatsapp lottery", "facebook lottery",
    "pay ₹1 to claim", "pay ₹10 to win",
    "lucky customer", "selected for prize",
    "your account is on hold", "your pan is blocked",
    "call this number", "urgent verification required",
    "you are selected", "act now", "limited time offer"
    ]
    safe_patterns = [
        "otp है", "otp:", "your otp", "पैमेंट सफल", "बिल सफल", "बुकिंग", "कन्फर्म", "सफलतापूर्वक", "Sucessfull" , "www.jio.com",
    "www.airtel.in",
    "www.amazon.in",
    "www.flipkart.com",
    "www.irctc.co.in",
    "uidai.gov.in",                # Aadhaar
    "incometax.gov.in",           # Income Tax
    "sbi.co.in",                  # State Bank of India
    "axisbank.com",
    "hdfcbank.com",
    "icicibank.com",
    "kotak.com",
    "yesbank.in",
    "paytm.com",
    "phonepe.com",
    "google.com/pay",            # Google Pay
    "npci.org.in",               # UPI backend
    "bhimupi.org.in",
    "digilocker.gov.in",
    "mygov.in",
    "echallan.parivahan.gov.in",  # Traffic challan
    "mparivahan.gov.in",
    "epfindia.gov.in",           # PF
    "myelectricitybill.com",     # Utility (verify per state)
    "timesofindia.indiatimes.com",  # News
    "ndtv.com",
    "moneycontrol.com",
    "angleone.com"
    "zerodha.com",               # Stock broker
    "groww.in",
    "angelone.in",
    "coinmarketcap.com",  
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
