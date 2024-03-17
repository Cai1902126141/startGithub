import os
import openai
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)
print(client.api_key)


def new_completion(user_message,system_message, model="gpt-3.5-turbo"):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message},           
        ],
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content
    
system_message = "be a helpful assistant"
user_message = "Say this is a test."
response = new_completion(user_message,system_message)
print(response)
