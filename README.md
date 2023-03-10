# Chat GPT R&D

#### Getting Started with Chat GPT Python API
- Install Python 3
- Install openai library: pip install openai
- Create account on https://platform.openai.com/overview
- Setup payment method and get API key
- Write python code

##### Chat GPT Hello World
```Python
import openai

openai.api_key = 'paste your api key here'

message = "What is the distance to sun in kilometers?"
messages = [{"role": "user", "content": message}]
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

print(completion.choices[0].message.content)
```

##### Chat GPT basic setup
```Python
import openai

openai.api_key = 'paste your api key here'

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
```