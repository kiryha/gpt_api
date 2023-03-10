import openai
import os
from open_api_key import OPEN_API_KEY
from PySide2 import QtWidgets, QtCore, QtGui
from ui import chat_gpt_main

openai.api_key = OPEN_API_KEY
root = os.path.dirname(os.path.abspath(__file__))

# messages = []
# message = input('Chat GPT: How can I assist you today?')
# if message:
#     messages.append({"role": "user", "content": message})
#
# while True:
#     message = input('User: ')
#     if message:
#         messages.append({'role': 'user', 'content': message})
#         completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
#         reply = completion.choices[0].message.content
#         print(f'Chat GPT: {reply}')
#         messages.append({'role': 'assistant', 'content': reply})


class ChatGPT(QtWidgets.QMainWindow, chat_gpt_main.Ui_ChatGPT):
    def __init__(self):
        super(ChatGPT, self).__init__()
        self.setupUi(self)
        self.spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.init_ui()

        self.btn_test.clicked.connect(self.execute)

    def init_ui(self):
        self.layout.addWidget(QtWidgets.QPushButton('A_WIN'))
        self.layout.addItem(self.spacer)

    def execute(self):
        self.layout.addWidget(QtWidgets.QPushButton('B_WIN'))



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    gpt = ChatGPT()
    gpt.setWindowIcon(QtGui.QIcon('{0}/icons/gpt.ico'.format(root)))
    gpt.show()
    app.exec_()
