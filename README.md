# 🌟 Flex Emotion Detection – AI Powered Flask Web App  
### 🔐 Login System + 😊 Face + ✍️ Handwriting + 🎤 Audio + 💬 Text Emotion Detection

Flex Emotion Detection is a **multi-AI emotion recognition web application** built with **Flask**, supporting:

✔ User Registration & Login  
✔ Face Emotion Detection (DeepFace)  
✔ Handwriting Emotion Detection (OCR + NLP)  
✔ Audio Emotion Detection (Wav2Vec2)  
✔ Text Emotion Detection (Roberta Emotion Model)  
✔ Session-based authentication  
✔ Works locally & on servers (supports mobile browser too)

---

## 📌 Features

### 🔐 User Authentication
- Register using: **Name, Email, Mobile, Password**
- Login using: **Email OR Mobile**
- Stores secured session for each user
- Unauthorized users cannot access AI features

### 😊 Face Emotion Detection
Detects **dominant emotion** from webcam using **DeepFace**.  
Emotions include:

`Happy, Sad, Angry, Neutral, Surprise, Fear, Disgust`

### ✍️ Handwriting Emotion Detection
- Extract text from handwriting using **pytesseract OCR**
- Detect emotional tone using NLP model

### 🎤 Audio Emotion Detection
- Accepts user microphone audio (WebM)
- Converts to WAV via ffmpeg
- Emotion detection using **wav2vec2 audio model**

Fallback: Energy-based (High / Low Emotion)

### 💬 Text Emotion Detection
Analyzes emotional tone of text using **Roberta-based classifier**.

---

# 🛠️ Tech Stack

| Component | Technology |
|----------|-------------|
| Backend | Flask |
| Face Emotion | DeepFace |
| Handwriting OCR | pytesseract |
| NLP Emotion | Transformers (Roberta Model) |
| Audio Emotion | Wav2Vec2 (superb/wav2vec2-base-superb-er) |
| Front-End | HTML, CSS, JavaScript |
| Database | JSON file (`users.json`) |

---

# 📥 Installation Guide

## 1️⃣ Clone This Repository
```bash
git clone https://github.com/YOUR_USERNAME/Flex-Emotion-Detection.git
cd Flex-Emotion-Detection
