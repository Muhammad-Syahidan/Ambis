from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    messages=[
        {"role": "user", "content": "Apa itu python?"}
    ],
    model="gpt-3.5-turbo"
)

print(response.choices[0].message.content)