from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)


def get_ai_response(prompt):

    response = client.chat.completions.create(

        model="openai/gpt-oss-20b:free",

        messages=[
            {
                "role": "system",
                "content": "You are a smart multilingual AI assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.7,
        max_tokens=800
    )

    return response.choices[0].message.content