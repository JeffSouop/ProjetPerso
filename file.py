# import the OpenAI Python library for calling the OpenAI API
from openai import OpenAI
import os

client = OpenAI(api_key='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')

# openai.api_key = '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'

# Example OpenAI Python library request
MODEL = "gpt-3.5-turbo"
response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
    ],
    temperature=0,
)

response.choices[0].message.content
