
import os
from openai import OpenAI

user_prompt = "Tell me interesting facts about Jack Russell?"

try:

    client = OpenAI(
        api_key = os.environ.get("ACCESS_KEY"),   
    )

    completion = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_prompt},
    ]
    )
    print('============================================================')    
    print(completion.choices[0].message.content.strip())
    print('============================================================')

except Exception as e:
    print(e)