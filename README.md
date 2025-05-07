# 🎙️ Voice Mail System for Visually Challenged People

This is an assistive technology project that allows visually impaired users to **send and receive voice messages** using a fully voice-driven interface. It eliminates the need for visual or text-based interaction.

---

## ✨ Features

- 📤 Voice message recording and sending
- 📥 Voice message playback for received messages
- 🔊 Text-to-speech (TTS) prompts
- 🎤 Speech-to-text (STT) recognition for commands

---

## 🛠️ Tech Stack

- Python
- SpeechRecognition
- gTTS or pyttsx3 (text-to-speech)
- pyaudio or sounddevice (for voice recording)
- Flask (optional, for UI/API if needed)

---

## 📦 Setup Instructions

```bash
git clone https://github.com/yourusername/voice_mail_system.git
cd voice_mail_system
pip install -r requirements.txt
python app/main.py
