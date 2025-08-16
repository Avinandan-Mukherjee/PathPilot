import google.generativeai as genai

import pyttsx3
import speech_recognition as sr

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


    def speech_to_text():
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Speak Now >>>>  ")
            r.adjust_for_ambient_noise(source)  
            audio = r.listen(source)  


        text = r.recognize_google(audio, language="en-IN")
        return text

        
        #for saving the audio
        #with open("input.wav", "wb") as f:
            #f.write(audio.get_wav_data())


    


    def text_to_speech(text):
        engine = pyttsx3.init()

        voices = engine.getProperty('voices')


        engine.setProperty('voice', voices[1].id) #1 is female voice


        engine.say(text)
        engine.runAndWait()





    def gemini():
        global log
        log = []
        behaviour = """ 
        You are a job interviewer AI. You will:
        - Ask the participant interview questions one by one.
        - Continue the interview for a random natural length (between 2 and 15 minutes).
        - After each answer, decide if you want to continue or end, but there should be a proper closure, and link to previous messages.
        - STRICT RULE: Every response must follow this format exactly:

        <True/False> -+continue+- <your response text here>

        Examples:
        True -+continue+- Can you tell me about your strengths?
        True -+continue+- What challenges have you overcome recently?
        False -+continue+- Thank you, the interview is over. Have a great day!


        when u are ending the interview, after the last message, change always type False in that first word area.
        Never break this format.
        """


        model = genai.GenerativeModel('gemini-2.5-flash') 
        chat = model.start_chat(
            history=[
                {'role': 'user', 'parts': [{'text': behaviour}]},
                {'role': 'model', 'parts': [{'text': 'I will follow the instructions'}]}
            ]
        )

        for z in range(5):
            inp = speech_to_text()
            response = chat.send_message(inp)
            split = response.text.split('-+continue+-')
            print(split[1])


            text_to_speech(split[1])

            log+=(
                f"Participant: {inp}",f"Interviewer: {split[1]}"
            )

            if (  (split[0]).strip() == 'False'   ):
                break;

        
        



    def score(log):
        behave = f""" Your Job is to analyse this job interview session, and give your feedback on it. Give a proper feedback, With points out of ten on various behalfs like grammer and all... and give areas to improve.  The interview: {log}"""
        print(log)

        response = model.generate_content(behave)
        print(response.text)
    gemini()
    score(log)
interview()