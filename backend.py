import google.generativeai as genai
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
    behave = f""" 
    Your task is to ask the user interview questions. His skills r. You will randomly keep the interview between 5-30 mins. Keep it professonal, and before ending, say a proper closure.    
    """