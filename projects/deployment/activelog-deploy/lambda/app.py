import os
import openai
import boto3
import requests
from dotenv import load_dotenv

load_dotenv()

def handler(event=None, context=None):
    print("Agent triggered.")
    
    # Example: fetch a value from config
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return {"error": "Missing OPENAI_API_KEY in environment"}

    openai.api_key = api_key

    # Example OpenAI call
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Hello from activelog!"}]
    )

    return {"response": response.choices[0].message["content"]}