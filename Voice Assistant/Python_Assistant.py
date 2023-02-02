import pyttsx3  # text to speech
import speech_recognition as sr  # speech recognization module and alised as sr
import pyjokes
import datetime
import webbrowser

# Make a function which gona convert your speech to text


def speech_to_text():

    # Create a object to store the class of speech recognization
    Recognizer = sr.Recognizer()

    # Take voice from user as a source
    with sr.Microphone() as source:

        # Give your user a Message of listening
        print("Listening........")

        # Avoid noise of source whichis actually coming from the microphone
        Recognizer.adjust_for_ambient_noise(source)

        # listen the audio from user and it's recorded in audio variable
        audio = Recognizer.listen(source)

        try:
            print("Recognizing......")

            # Data should be audio recognized
            data = Recognizer.recognize_google(audio)
            print(data)

        # Rasie and error if it does not recognize
        except sr.UnknownValueError:
            print("Not understanding ")


# speech_to_text()


def text_to_speech(x):
    # Make a variable / object to call the class of the pyttsx3
    Engine = pyttsx3.init()
    voices = Engine.getProperty("voices")
    # Voice of male if 0
    # Voice of female if 1
    Engine.setProperty("voice", voices[1].id)

    # Decrease the speed of voice
    rate = Engine.setProperty('rate', 100)
    Engine.setProperty('rate', 150)

    # Return your message into voice using say function
    Engine.say(x)
    Engine.runAndWait()


text_to_speech("Tu banda ban ja ")
# text_to_speech("Get your online store up and running with our e-commerce services on Fiverr. Our team of experts will help you set up a user-friendly, customized e-commerce platform to help you sell your products or services online. We specialize in popular platforms such as Shopify, WooCommerce, and Magento, and can provide everything from setup and configuration to theme customization and payment gateway integration. Trust us to deliver a seamless online shopping experience for your customers.")
