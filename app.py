from flask import Flask, request, jsonify, render_template, session, redirect, url_for
from PIL import Image
import io
import numpy as np
from deepface import DeepFace
import pytesseract
from transformers import pipeline
import librosa
import os
import json

# Initialize Flask App
app = Flask(__name__)
app.secret_key = "super_secret_key_change_this"  # Required for Session Management

# Database File
DB_FILE = 'users.json'

# Helper: Load Users
def load_users():
    if not os.path.exists(DB_FILE):
        return []
    try:
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

# Helper: Save Users
def save_users(users):
    with open(DB_FILE, 'w') as f:
        json.dump(users, f, indent=4)

# --- LOAD AI MODELS (Same as before) ---
try:
    text_pipe = pipeline('text-classification', model='j-hartmann/emotion-english-distilroberta-base')
    audio_pipe = pipeline('audio-classification', model='superb/wav2vec2-base-superb-er')
    print("Models loaded successfully.")
except Exception as e:
    print(f"Error loading models: {e}")

# --- ROUTES ---

@app.route("/")
def index():
    # Check if user is logged in
    user = session.get('user')
    return render_template("index.html", user=user)

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    mobile = data.get('mobile')
    password = data.get('password')

    if not all([name, email, mobile, password]):
        return jsonify({"success": False, "message": "All fields are required."})

    users = load_users()

    # Check for unique email and mobile
    for user in users:
        if user['email'] == email:
            return jsonify({"success": False, "message": "Email already exists."})
        if user['mobile'] == mobile:
            return jsonify({"success": False, "message": "Mobile number already exists."})

    # Add new user
    new_user = {
        "name": name,
        "email": email,
        "mobile": mobile,
        "password": password  # In production, hash this password!
    }
    users.append(new_user)
    save_users(users)

    return jsonify({"success": True, "message": "Registration successful! Please login."})

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    identifier = data.get('identifier') # Can be email or mobile
    password = data.get('password')

    users = load_users()
    
    user_found = None
    for user in users:
        # Check against email OR mobile
        if (user['email'] == identifier or user['mobile'] == identifier) and user['password'] == password:
            user_found = user
            break

    if user_found:
        session['user'] = user_found['name']
        return jsonify({"success": True, "message": "Login successful!"})
    else:
        return jsonify({"success": False, "message": "Invalid Credentials."})

@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

# --- EXISTING ANALYSIS ROUTES (Unchanged) ---

@app.route("/analyze_face", methods=["POST"])
def analyze_face():
    if 'user' not in session: return jsonify({"error": "Unauthorized"}), 401
    f = request.files.get('frame')
    if not f: return jsonify({"error": "No frame received"}), 400
    try:
        img = Image.open(io.BytesIO(f.read())).convert("RGB")
        npimg = np.array(img)
        result = DeepFace.analyze(npimg, actions=['emotion'], enforce_detection=False)
        if isinstance(result, list): result = result[0]
        dominant_emotion = result.get("dominant_emotion", "Not detected")
        return jsonify({"emotion": dominant_emotion.capitalize()})
    except Exception as e:
        return jsonify({"emotion": "Error"}), 500

@app.route("/analyze_handwriting", methods=["POST"])
def analyze_hand():
    if 'user' not in session: return jsonify({"error": "Unauthorized"}), 401
    f = request.files.get('hand')
    if not f: return jsonify({"error": "No image received"}), 400
    try:
        img = Image.open(io.BytesIO(f.read())).convert("L")
        text = pytesseract.image_to_string(img).strip()
        emotion = "No text found"
        if text:
            out = text_pipe(text)[0]
            emotion = out["label"].capitalize()
        return jsonify({"text": text, "emotion": emotion})
    except Exception as e:
        return jsonify({"text": "", "emotion": "Error"}), 500

@app.route("/analyze_audio", methods=["POST"])
def analyze_audio():
    if 'user' not in session: return jsonify({"error": "Unauthorized"}), 401
    f = request.files.get("audio")
    if not f: return jsonify({"error": "No audio received"}), 400
    webm_path = "temp_audio.webm"
    wav_path = "temp_audio.wav"
    with open(webm_path, "wb") as out: out.write(f.read())
    emotion = "N/A"
    try:
        os.system(f"ffmpeg -y -i {webm_path} -ar 16000 -ac 1 -c:a pcm_s16le {wav_path}")
        out = audio_pipe(wav_path)[0]
        emotion = out["label"].capitalize()
    except:
        try:
            y, sr = librosa.load(wav_path, sr=16000)
            energy = float(np.mean(np.abs(y)))
            emotion = "High Energy" if energy > 0.02 else "Low Energy"
        except: emotion = "Failed"
    finally:
        if os.path.exists(webm_path): os.remove(webm_path)
        if os.path.exists(wav_path): os.remove(wav_path)
    return jsonify({"emotion": emotion})

@app.route("/analyze_text", methods=["POST"])
def analyze_text():
    if 'user' not in session: return jsonify({"error": "Unauthorized"}), 401
    data = request.get_json()
    text = data.get('text', '').strip()
    try:
        out = text_pipe(text)[0]
        return jsonify({"emotion": out["label"].capitalize()})
    except Exception:
        return jsonify({"emotion": "Error"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)