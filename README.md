# Chat GPT Python API First Steps
![](./gpt_api/images/chat_gpt.png)

#### Getting Started with Chat GPT Python API
- Install Python 3. Notice where it was installed. 
Mine is in `C:\Users\username\AppData\Local\Programs\Python\Python310\`, I am on Windows,
for another OS things can be quite different.

- Install "openai" python library: launch Command Prompt window and run command `pip install openai`
If you succeed those steps the chances to get to the finish are quite high for you :)

- Create account on https://platform.openai.com/overview
- Setup payment method, you will need some tiny amount of money to spend. 
- Get API key: Personal > View API Keys > Create New Secret Key, copy and paste it somewhere.
- Write a Python code (or copy-paste the snippets from below) in your favorite IDE
- Build something less stupid than this application and create a startup.

##### Chat GPT Hello World
```Python
import openai

openai.api_key = 'paste your api key here'

message = "What is the distance to sun?"
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

##### Chat GPT UI example (gpt_api.py)
###### How to run
Download and unzip repository to your local folder.

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