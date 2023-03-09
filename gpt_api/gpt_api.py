import openai
from open_api_key import OPEN_API_KEY

openai.api_key = OPEN_API_KEY

message = "What is the distance to sun in kilometers?"
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": message}])

print(completion.choices[0].message.content)