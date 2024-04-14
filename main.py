import config
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=config.API_KEY,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Cuál es la misión de OpenAI?",
        }
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion)