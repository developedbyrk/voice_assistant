import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import myApiKeys

recognizer = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

newsapikey = myApiKeys.newsApi

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapikey}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            for article in articles:
                speak(article.get("title"))

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    
    while True:
        r = sr.Recognizer()

        try:
            with sr.Microphone() as source:
                # wake up jarvis
                print("Listening...")
                audio = r.listen(source)
                print("Recognizing...")

                word = r.recognize_google(audio)

                if word.lower() == 'jarvis':
                    speak("Yes sir")

                    # Listen for command
                    with sr.Microphone() as source:
                        print("Jarvis Active")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)
                        print(command)
                        processCommand(command)
        except:
            print("Sorry, I did not get that")