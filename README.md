# 🗣️ Voice Assistant "Nova" 🔊

A simple yet powerful Python voice assistant project named **Nova**, capable of recognizing speech, responding with voice, performing online searches, playing music, reading news, and answering questions using **Google Gemini**.

---

## 🚀 Features

- ✅ Voice activation via keyword ("Nova")
- ✅ Open popular websites via voice command
- ✅ Search Google with custom queries
- ✅ Play music from a predefined music library
- ✅ Read top headlines from NewsAPI
- ✅ Respond to custom questions using **Google Gemini**
- ✅ Voice feedback using `pyttsx3`
- ✅ Exit via "stop listening" voice command

---

## 🛠️ Technologies & Libraries Used

- Python 3
- `speech_recognition` – for capturing and recognizing voice input
- `pyttsx3` – for text-to-speech voice output
- `webbrowser` – to open sites in default browser
- `requests` – for fetching news via API
- `google.generativeai` – to connect with Google Gemini API
- `NewsAPI.org` – for latest news
- `Microphone` – for real-time speech input

---

## 📁 Project Structure

voice_assistant/
├── voice_assistant.py
├── musicLibrary.py # Your custom music dictionary
├── myApiKeys.py # API keys for NewsAPI and Gemini
└── README.md
