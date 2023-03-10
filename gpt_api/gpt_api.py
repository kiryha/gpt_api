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


class ChatModel(QtCore.QAbstractTableModel):
    def __init__(self, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.header = ['How can I assist you today?']

    def flags(self, index):

        column = index.column()
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header[0]

    def rowCount(self, parent):

        return 100

    def columnCount(self, parent):

        return 1

    def data(self, index, role):

        if not index.isValid():
            return

        row = index.row()
        column = index.column()

        if role == QtCore.Qt.BackgroundRole:
            if row % 2 == 0:
                return QtGui.QBrush(QtGui.QColor('#f2f2f2'))

        # if role == QtCore.Qt.DisplayRole:
        #     return 'AA'


class ChatGPT(QtWidgets.QMainWindow, chat_gpt_main.Ui_ChatGPT):
    def __init__(self):
        super(ChatGPT, self).__init__()
        self.setupUi(self)
        self.init_ui()

        self.btn_test.clicked.connect(self.execute)

    def init_ui(self):

        self.tab_chat.verticalHeader().hide()
        self.tab_chat.verticalHeader().ResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.tab_chat.horizontalHeader().ResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.tab_chat.horizontalHeader().setStretchLastSection(True)

        self.chat_model = ChatModel()
        self.tab_chat.setModel(self.chat_model)

    def execute(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    gpt = ChatGPT()
    gpt.setWindowIcon(QtGui.QIcon('{0}/icons/gpt.ico'.format(root)))
    gpt.show()
    app.exec_()
