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
```






Create Virtual Environment (Recommended)
Windows:
```
python -m venv venv
venv\Scripts\activate
```
Linux / Mac:
```
python3 -m venv venv
source venv/bin/activate
```
3️⃣ Install Dependencies

Install all required modules using:
```
pip install -r requirements.txt
```
📦 requirements.txt (Included)
```
Flask
deepface
pillow
numpy
pytesseract
transformers
torch
librosa
soundfile
opencv-python
tf-keras
protobuf==3.20.*
sentencepiece
requests
```

Note: json is not included because it is built-in.

4️⃣ Install Tesseract OCR (Important)
Ubuntu/Debian:
sudo apt install tesseract-ocr
sudo apt install ffmpeg

Windows:

Download & Install Tesseract:
https://github.com/UB-Mannheim/tesseract/wiki

5️⃣ Run the App
python app.py

6️⃣ Open in Browser

Local access:

http://localhost:5000


Mobile access (same WiFi):

http://YOUR_LOCAL_IP:5000


Public access:

http://YOUR_SERVER_IP:5000

📁 Project Structure
Flex-Emotion-Detection/
│── app.py
│── users.json
│── requirements.txt
│── templates/
│     └── index.html
│── static/
      ├── css/
      ├── js/
      └── images/

🔐 API Routes
🧑‍💻 Authentication
Method	Route	Description
POST	/register	Register new user
POST	/login	Login using email/mobile
GET	/logout	Logout
Login Body Example
{
  "identifier": "email_or_mobile",
  "password": "password123"
}

🎯 Emotion Detection Routes (Protected)
Method	Route	Description
POST	/analyze_face	Detect emotion from webcam frame
POST	/analyze_handwriting	Detect handwriting emotion
POST	/analyze_audio	Detect audio emotion
POST	/analyze_text	Detect text emotion
🌐 Deploy on VPS (Ubuntu)

Install dependencies:

sudo apt update
sudo apt install python3 python3-pip python3-venv nginx ffmpeg tesseract-ocr -y

Run with Gunicorn + PM2
pip install gunicorn
pm2 start "gunicorn -b 0.0.0.0:5000 app:app"
pm2 startup
pm2 save

Configure Nginx
sudo nano /etc/nginx/sites-enabled/emotion.conf


Add:

server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}


Restart Nginx:

sudo systemctl restart nginx









