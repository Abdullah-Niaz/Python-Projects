import openai
import speech_recognition as sr

listener = sr.Recognizer()
openai.api_key = "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"

while True:
  with sr.Microphone() as source:
    print("Speek Now.....")
    voice = listener.listen(source)
    print(voice)
    data = listener.recognize_google(voice)
    model = "text-davinci-003" 
    # models
    if "exit" in data:
      break
        
  
  completion = openai.Completion.create(model = "text-davinci-003",
    prompt= data,
    max_tokens= 1024,
    temperature= 0.5,
    n= 1,
    stop = None)
  # print the completion
  response = completion.choices[0].text
  print(response)