import pyttsx3  # Text-to-speech
import speech_recognition as sr  # Speech recognition module
import pyjokes
import datetime
import webbrowser
import os
import time

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not understanding")

def text_to_speech(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    while True:
        user_input = speech_to_text().lower()
        if "your name" in user_input:
            text_to_speech("My name is Alexa")
        elif "your age" in user_input:
            text_to_speech("I'm a computer program, so I don't have an age.")
        elif "bad egg" in user_input:
            text_to_speech("I'm not a bad egg.")
        elif "time" in user_input:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            text_to_speech(f"The current time is {current_time}")
        elif "youtube" in user_input:
            webbrowser.open("https://www.youtube.com")
        elif "joke" in user_input:
            joke = pyjokes.get_joke(language="en", category="neutral")
            print(joke)
            text_to_speech(joke)
        elif "play a song" in user_input:
            music_folder = "D:/songs"
            song_list = os.listdir(music_folder)
            if song_list:
                os.startfile(os.path.join(music_folder, song_list[0]))
            else:
                text_to_speech("No songs found in the music folder.")
        elif "exit" in user_input:
            text_to_speech("Thank you! See you again.")
            break
        time.sleep(5)
