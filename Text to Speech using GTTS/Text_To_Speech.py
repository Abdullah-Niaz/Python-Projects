from gtts import gTTS
import mpyg321
import os

# text = "Get your online store up and running with our e-commerce services on Fiverr. Our team of experts will help you set up a user-friendly, customized e-commerce platform to help you sell your products or services online. We specialize in popular platforms such as Shopify, WooCommerce, and Magento, and can provide everything from setup and configuration to theme customization and payment gateway integration. Trust us to deliver a seamless online shopping experience for your customers."
text = "Hello, I am a student of education university, pursuing my computer science degree"
# Convert text to speech
tts = gTTS(text)

# Save audio file

tts.save("D:\PS\python-projects\Text to Speech using GTTS\Store.mp3")

# Play audio file
os.system("start Store.mp3")
