import openai
import os
from open_api_key import OPEN_API_KEY
from PySide2 import QtWidgets, QtGui
from ui import chat_gpt_main


class ChatGPT(QtWidgets.QMainWindow, chat_gpt_main.Ui_ChatGPT):
    def __init__(self):
        super(ChatGPT, self).__init__()
        self.setupUi(self)

        self.messages = []

        self.init_ui()

        self.start_new.clicked.connect(self.start_new_chat)
        self.message.returnPressed.connect(self.send_message)

    def init_ui(self):

        # Initiate conversation
        self.chat.append('Ghat GPT: How can I assist you today?\n')
        self.message.setFocus()

    def start_new_chat(self):

        # Reset conversation
        self.messages = []
        self.chat.clear()
        self.init_ui()

    def send_message(self):

        # Get user message
        user_message = self.message.text()
        self.chat.append(f'User: {user_message}\n')
        self.message.clear()

        # Send request to Chat GPT and show reply in UI
        self.messages.append({'role': 'user', 'content': user_message})
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=self.messages)
        reply = completion.choices[0].message.content
        self.chat.append(f'Chat GPT: {reply}\n')
        self.messages.append({'role': 'assistant', 'content': reply})


if __name__ == "__main__":
    openai.api_key = OPEN_API_KEY
    root = os.path.dirname(os.path.abspath(__file__))
    app = QtWidgets.QApplication([])
    gpt = ChatGPT()
    gpt.setWindowIcon(QtGui.QIcon('{0}/icons/gpt.ico'.format(root)))
    gpt.show()
    app.exec_()
