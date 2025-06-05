import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-pro") 

def summarize_biological_data(text: str) -> str:
    #response = model.generate_content(text)
   # return response.text.strip()
    print("MOCKING LLM RESPONSE")
    return "This is a mocked summary for demonstration purposes."
