import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import musicLibrary

from google import genai
import myApiKeys # Local file which contains api keys (News and Gemini)

# news api key to get the news
newsapikey = myApiKeys.newsApi

# speech recognizer
# recognizer = sr.Recognizer()

# text to speak engine initializing
engine = pyttsx3.init()

# get the voices
voices = engine.getProperty('voices')

# changed engine voice to female voice
engine.setProperty('voice', voices[1].id)

# variable for the while loop to stop conditionally
running = True

# speak funciton using pyttsx3
def speak(text):
    engine.say(text)
    engine.runAndWait()

# process command function for all the instruction
# if any conditon is true to open in broswer it will work
# otherwise it will give the result with Google Gemini, can ask anything.
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
        res = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapikey}")
        if res.status_code == 200:
            data = res.json()
            articles = data.get("articles", [])
            for article in articles:
                speak(article.get("title"))

    elif "search" in c.lower():
        query = c.replace(" ", "+")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    else:
        # if none of other consition is True & not deactivating the voive assistant
        # Google Gemini will answer your query, ask anything.
        client = genai.Client(api_key=myApiKeys.gKey)
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=c
        )
        print(response.text)
        speak(response.text)

if __name__ == "__main__":
    speak("Initializing voice assistant...")

    while running:
        recognizer = sr.Recognizer()

        try:
            with sr.Microphone() as source:
                # Activate the voice assistant 
                print("Listening...")
                audio = recognizer.listen(source, timeout=2)
                print("Recognizing...")

                word = recognizer.recognize_google(audio)

                # Assistant will be active by listining her name
                assistant_name = "nova"

                # if word.lower() == assistant_name:
                if assistant_name in word.lower():
                    speak(f"Hello, {assistant_name} is here, your voice assistant.")

                    # Listen for command
                    with sr.Microphone() as source:
                        print(f"{assistant_name.capitalize()} is active & listening...")

                        audio = recognizer.listen(source)
                        command = recognizer.recognize_google(audio)

                        print(command)
                        processCommand(command)

                # exit the program with "stop listening" command
                if "stop listening" in word.lower():
                    print("Voice assistant deactivated. Exiting program.")
                    running = False
                        
        except:
            print("Sorry, I did not get that")


