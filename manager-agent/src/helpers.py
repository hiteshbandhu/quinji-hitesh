from os import getenv
from openai import OpenAI

client = OpenAI(api_key=getenv("OPENAI_API_KEY"))

def get_llm_response(prompt:str):
    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
    )

    return completion.choices[0].message.content