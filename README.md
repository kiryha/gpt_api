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

##### Chat GPT command line conversation
```Python
import openai

openai.api_key = 'paste your api key here'

print('Chat GPT: How can I assist you today?')

messages = []
while True:
    message = input('User: ')
    if message:
        messages.append({'role': 'user', 'content': message})
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply = completion.choices[0].message.content
        print(f'Chat GPT: {reply}')
        messages.append({'role': 'assistant', 'content': reply})
```

##### Chat GPT UI example
###### How to run
Download and unzip repository to your local folder.
Alternatively, can install "GitHub Desktop" application and clone this repo to your local drive. 

Create open_api_key.py file next to chat_gpt.py and record you API key there:

```Python
OPEN_API_KEY = 'your API key'
```

Modify run_chat_gpt.bat with your path to Python3 install dir. Double click run_chat_gpt.bat to launch application.

###### How to modify
To be able to edit UI file as you need, modify _compile_ui.bat with your path to pyside2-uic.exe.
Edit UI file chat_gpt_main.ui with QTDesigner, save, drag and drop on _compile_ui.bat to update changes.

QTDesigner located in: `YourPython3Folder\Lib\site-packages\PySide2\designer.exe`

Edit code, run the gpt_api.py, enjoy :)