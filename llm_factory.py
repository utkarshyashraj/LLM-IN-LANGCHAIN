import os #used to access environment variables
import json #used to load configuration from config.json
from dotenv import load_dotenv #used to load environment variables from .env file
from langchain_google_genai import ChatGoogleGenerativeAI #used to access the Gemini model from Google Generative AI

load_dotenv()

#Load configuration from config.json
with open("config.json", "r") as f:
    config = json.load(f)   
provider=config["provider"]

#Intialize the model based on the provider specified in config.json
def get_llm():
    if provider=="gemini":
        llm = ChatGoogleGenerativeAI(model=config["gemini"]["model"],
                                     temperature=config["gemini"]["temperature"],
                                     max_output_tokens=config["gemini"]["max_output_tokens"],
                                     api_key=os.getenv("GEMINI_API_KEY"))
    else:
        raise ValueError("Invalid provider specified in config.json. Please use 'gemini' as the provider.")
    return llm