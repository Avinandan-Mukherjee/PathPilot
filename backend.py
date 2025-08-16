import google.generativeai as genai

import pyttsx3
import speech_recognition as sr
import whisper

from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("GEMINI_API")

genai.configure(api_key= api_key)

model = genai.GenerativeModel('gemini-2.5-flash')







def chat():
    behave = f""" 
    You r a bot made for guiding people on their career.  
    """

    response = model.generate_content(behave)

    print(response.text)


def interview():


    def record():
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Speak Now >>>>  ")
            r.adjust_for_ambient_noise(source)  
            audio = r.listen(source)  
            
        print("Done recording")


        text = r.recognize_google(audio, language="en-IN")
        print(text)

        
        #for saving the audio
        #with open("input.wav", "wb") as f:
            #f.write(audio.get_wav_data())


    


    def text_to_speech():
        engine = pyttsx3.init()

        voices = engine.getProperty('voices')


        engine.setProperty('voice', voices[1].id) #1 is female voice


        engine.say("Hello Brother how r u")
        engine.runAndWait()


    
    record()

interview()