import openai
from open_api_key import OPEN_API_KEY

openai.api_key = OPEN_API_KEY

# completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": '2+3=?'}])
# print(completion.choices[0].message.content)

messages = []
message = input('Chat GPT: How can I assist you today?')
if message:
    messages.append({"role": "user", "content": message})

while True:
    message = input('User: ')
    if message:
        messages.append({'role': 'user', 'content': message})
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply = completion.choices[0].message.content
        print(f'Chat GPT: {reply}')
        messages.append({'role': 'assistant', 'content': reply})


