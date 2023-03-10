# Chat GPT R&D

#### Getting Started with Chat GPT Python API
- Install Python 3
- Install openai library: pip install openai
- Create account on https://platform.openai.com/overview
- Setup payment method and get API key
- Write python code

##### The basic example
```Python
import openai
import open_api_key

openai.api_key = 'paste your api key here'

message = "What is the distance to sun in kilometers?"
messages = [{"role": "user", "content": message}]
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
print(completion.choices[0].message.content)
```