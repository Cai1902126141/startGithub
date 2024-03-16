#import openai
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

print(openai.api_key)



# 创建一个 GPT-3 请求
response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Please provide some tips for beginner Python programmers.",
    temperature=0.7,
    max_tokens=50,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# 输出 GPT-3 的回答
print(response.choices[0].text.strip())

