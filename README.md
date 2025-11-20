# 🌟 Flex Emotion Detection – AI Powered Flask Web App  
### 🔐 Login System + 😊 Face + ✍️ Handwriting + 🎤 Audio + 💬 Text Emotion Detection

Flex Emotion Detection is a powerful **multi-AI emotional analysis web application** built using **Flask**.  
It supports emotion detection from:

- Face (via webcam)
- Handwriting (OCR + NLP)
- Audio (Wav2Vec2 audio model)
- Text (Roberta-based NLP model)

The app includes a secure **user registration & login system** with session-based access control.

---

# 📌 Features

### 🔐 User Authentication
- Register with **Name, Email, Mobile, Password**
- Login using **Email OR Mobile**
- Secure session login system
- Prevents unauthorized access

### 😊 Face Emotion Detection
Uses **DeepFace** to analyze emotions from webcam images.

### ✍️ Handwriting Emotion Detection
- Extracts text using **Tesseract OCR**
- Detects emotional tone using NLP

### 🎤 Audio Emotion Detection
- Uses ffmpeg to convert audio
- Emotion detection with **Wav2Vec2**
- Fallback: Energy-based emotion

### 💬 Text Emotion Detection
Uses a **Roberta emotion model** for text emotion classification.

---

# 🛠️ Tech Stack

| Component | Technology |
|----------|-------------|
| Backend | Flask |
| Face Emotion | DeepFace |
| OCR | Pytesseract |
| NLP | Transformers |
| Audio Emotion | Wav2Vec2 |
| Front-End | HTML, CSS, JS |
| Database | users.json |

---

# 📥 Installation Guide

Follow these steps to install and run the project.

---

## 1️⃣ Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/Flex-Emotion-Detection.git
cd Flex-Emotion-Detection
