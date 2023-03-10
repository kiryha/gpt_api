import openai
import os
from open_api_key import OPEN_API_KEY
from PySide2 import QtWidgets, QtCore, QtGui
from ui import chat_gpt_main


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


class ChatGPT:
    def __init__(self):
        self.messages = []

    def add_user_message(self, message):

        self.messages.append({"role": "user", "content": message})
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=self.messages)
        reply = completion.choices[0].message.content
        self.messages.append({'role': 'assistant', 'content': reply})

        return reply


class ChatModel(QtCore.QAbstractTableModel):
    def __init__(self, chat_gpt):
        QtCore.QAbstractTableModel.__init__(self)
        self.chat_gpt = chat_gpt
        self.header = ['How can I assist you today?']

    def flags(self, index):

        column = index.column()
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header[0]

    def rowCount(self, parent):

        return len(self.chat_gpt.messages) + 1

    def columnCount(self, parent):

        return 1

    def data(self, index, role):

        if not index.isValid():
            return

        row = index.row()

        if role == QtCore.Qt.BackgroundRole:
            if row % 2 == 0:
                return QtGui.QBrush(QtGui.QColor('#f2f2f2'))

        if role == QtCore.Qt.DisplayRole:
            if len(self.chat_gpt.messages) > row:
                return self.chat_gpt.messages[row]['content']

    def setData(self, index, cell_data, role=QtCore.Qt.EditRole):

        if role == QtCore.Qt.EditRole:

            print(self.chat_gpt.add_user_message(cell_data))
            return True


class ChatGPTMain(QtWidgets.QMainWindow, chat_gpt_main.Ui_ChatGPT):
    def __init__(self):
        super(ChatGPTMain, self).__init__()
        self.setupUi(self)
        self.chat_gpt = ChatGPT()
        self.chat_model = ChatModel(self.chat_gpt)

        self.init_ui()
        self.tab_chat.setModel(self.chat_model)

        self.btn_test.clicked.connect(self.update)
        self.tab_chat.clicked.connect(self.update)

    def init_ui(self):

        self.tab_chat.verticalHeader().hide()
        self.tab_chat.verticalHeader().ResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.tab_chat.horizontalHeader().ResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.tab_chat.horizontalHeader().setStretchLastSection(True)

    def update(self):
        self.chat_model.layoutChanged.emit()


if __name__ == "__main__":
    openai.api_key = OPEN_API_KEY
    root = os.path.dirname(os.path.abspath(__file__))
    app = QtWidgets.QApplication([])
    gpt = ChatGPTMain()
    gpt.setWindowIcon(QtGui.QIcon('{0}/icons/gpt.ico'.format(root)))
    gpt.show()
    app.exec_()
