# ai-emotion-detection
AI Emotion Detection



🌟 Flex Emotion Detection – AI Powered Flask App

A powerful AI-based Emotion Detection Web Application built using Flask, featuring:

✔ User Registration & Login (Email / Mobile + Password)
✔ Face Emotion Detection (Webcam) – DeepFace
✔ Handwriting Emotion Detection – OCR + NLP
✔ Audio Emotion Detection – wav2vec2 Audio Model
✔ Text Emotion Detection – Roberta Emotion Model
✔ Secure Session-Based Access
✔ Works on Desktop & Mobile Browser (locally or over server)

This project integrates multiple AI models (Vision, Audio, Text) to analyze and detect emotions from different inputs.

🚀 Features
🔐 User Authentication

Register using name, email, mobile, password

Login using email OR mobile

Sessions used for authentication

Secure route access (only logged-in users can analyze emotions)

😊 Face Emotion Detection

Uses DeepFace to detect dominant emotion from a captured webcam frame.

Emotions include:
happy, sad, angry, fear, surprise, neutral, etc.

✍️ Handwriting Emotion Detection

Extract text using pytesseract OCR

Analyze emotional tone using Roberta emotion model

🎤 Audio Emotion Detection

Uploaded audio (WebM) converted to WAV using ffmpeg

Analyzed using wav2vec2-base-superb-er

Fallback: If the model fails, system calculates energy of audio to give basic emotion classification.

💬 Text Emotion Detection

Direct text input processed using NLP emotion classifier.

🛠️ Tech Stack
Backend

Flask

DeepFace

Transformers (HuggingFace)

wav2vec2 Audio Emotion Model

pytesseract OCR

numpy, librosa

Frontend

HTML, CSS, JS

Webcam capture

Ajax-based API requests

📁 Project Structure
project/
│── app.py
│── users.json
│── requirements.txt
│── templates/
│     └── index.html
│── static/
      ├── css/
      ├── js/

▶️ How to Run
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Run Flask App
python app.py

3️⃣ Access in Browser
http://localhost:5000


To access from anywhere (public):

http://YOUR_SERVER_IP:5000

🔒 Default Security Notes

Passwords saved in plain JSON file (for demo)
→ Replace with hashed passwords for production

Use HTTPS for webcam & audio permissions

Not recommended for large-scale production use without upgrades

📸 Demo (What It Does)

Capture face → detects emotion

Upload handwriting → extracts text + emotion

Speak into mic → audio emotion

Type text → instant emotion detection

All features are unlocked after login.

🤝 Contributing

Pull requests are welcome!
Improve UI, add new emotion models, or integrate a database like MySQL or MongoDB.

📜 License

MIT License – free to use and modify.
