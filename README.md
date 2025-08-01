# 🛡️ Cyber Fraud Alert Assistant

A smart, multilingual fraud detection system that helps users identify scam messages in **English, Hindi, and Marathi** using a trained machine learning model and a Flutter-based mobile app.

---

## 📌 Project Highlights

- ✅ ML model trained on real-world Hindi, Marathi & English scam messages
- 📲 Flutter mobile app that interacts with the ML API
- 🔁 Real-time SMS detection (manual paste in v1, auto-SMS planned)
- 🧠 NLP + TF-IDF based classification (Scam or Legit)
- ☁️ Flask API hosted on Render for public access

---

## 📱 Flutter App Demo

> 🔎 Current version supports **manual pasting** of suspicious messages.
> Future versions will include auto SMS detection, pop-up warnings, and scam call monitoring.

### English Message Test

| Scam Example | Legit Example |
|--------------|---------------|
| ![Scam EN](./screenshots/scam_english.jpeg) | ![Legit EN](./screenshots/legit_english.jpeg) |

---

### Hindi Message Test

| Scam Example | Legit Example |
|--------------|---------------|
| ![Scam HI](./screenshots/scam_hindi.jpeg) | ![Legit HI](./screenshots/legit_hindi.jpeg) |

---

### Marathi Message Test

| Scam Example | Legit Example |
|--------------|---------------|
| ![Scam MR](./screenshots/scam_marathi.jpeg) | ![Legit MR](./screenshots/legit_marathi.jpeg) |

---

## 🔍 ML Model Details

- ✅ Preprocessing: Tokenization, stopword removal, lowercase normalization
- 📊 Features: TF-IDF vectors
- 🧠 Model: Logistic Regression (best accuracy after tuning)
- 🧪 Accuracy: ~95% on multilingual messages

---

## 🚀 Tech Stack

| Layer        | Tech Used                        |
|--------------|----------------------------------|
| 🧠 ML Model  | scikit-learn, pandas, nltk       |
| 🌐 API       | Flask, Python, Render Deployment |
| 📱 App       | Flutter, Dart                    |
| 📡 Communication | HTTP POST (JSON API)         |

---

## 🌟 Future Features & Ideas

| Feature                      | Description & Tools to Explore                                |
|-----------------------------|----------------------------------------------------------------|
| 📩 Auto SMS Detection        | `telephony` plugin (partially integrated)                      |
| 🔔 Pop-up Scam Alert         | `flutter_local_notifications`, background service              |
| 🧠 Fraud Call Detection      | `speech_to_text`, `Google Speech API`, `Vosk`, keyword spotting |
| 📹 Video Call Scam Detector  | `flutter_webrtc` + `flutter_audio_capture` + audio ML model    |
| 📊 Scan History              | Store past messages using SQLite (`sqflite` plugin)            |
| 🌐 Web Panel (optional)      | Add admin dashboard with analytics using Django + React        |

---

## 📦 Folder Structure

cyber-fraud-alert-assistant/
├── fraud_alert_app_new/ # Flutter App
├── fraud_detection_api/ # Flask API with ML model
├── saved_models/ # Trained ML model (pickle/vectorizer)
├── model_training_notebooks / # EDA and ML model
├── data / # datasets 
├── screenshots/ # Demo and architecture images
└── README.md


---

## 🤝 Credits

- Built by [Akash Sare](https://github.com/Akash-Sare03)
- Thanks to open-source contributors for libraries used

---

## 📬 Contact

For queries, reach out at: `akashsare03@gmail.com`
