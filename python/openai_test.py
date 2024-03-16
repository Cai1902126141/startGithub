import os
import openai
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)
print(OpenAI.api_key)


def new_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    completion = client.chat.completions.create(model=model,
                                                messages=messages, 
)
    return completion.choices[0].text.strip()
    

prompt = "Say this is a test."
response = new_completion(prompt)
print(response)
