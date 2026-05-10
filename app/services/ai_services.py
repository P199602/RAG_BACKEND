from openai import OpenAI

from dotenv import load_dotenv

import os

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)

def get_ai_response(question, context):

    prompt = f"""
    You are a helpful AI assistant.

    Answer from the provided context.

    If context is insufficient, reply naturally.

    Support:
    - Hindi
    - English
    - Hinglish

    Context:
    {context}

    Question:
    {question}
    """

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.7,
        max_tokens=1000
    )

    return response.choices[0].message.content