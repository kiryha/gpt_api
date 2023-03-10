# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chat_gpt_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ChatGPT(object):
    def setupUi(self, ChatGPT):
        if not ChatGPT.objectName():
            ChatGPT.setObjectName(u"ChatGPT")
        ChatGPT.resize(529, 543)
        self.centralwidget = QWidget(ChatGPT)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.chat = QTextEdit(self.centralwidget)
        self.chat.setObjectName(u"chat")

        self.verticalLayout.addWidget(self.chat)

        self.message = QLineEdit(self.centralwidget)
        self.message.setObjectName(u"message")

        self.verticalLayout.addWidget(self.message)

        self.start_new = QPushButton(self.centralwidget)
        self.start_new.setObjectName(u"start_new")

        self.verticalLayout.addWidget(self.start_new)

        ChatGPT.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ChatGPT)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 529, 21))
        ChatGPT.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ChatGPT)
        self.statusbar.setObjectName(u"statusbar")
        ChatGPT.setStatusBar(self.statusbar)

        self.retranslateUi(ChatGPT)

        QMetaObject.connectSlotsByName(ChatGPT)
    # setupUi

    def retranslateUi(self, ChatGPT):
        ChatGPT.setWindowTitle(QCoreApplication.translate("ChatGPT", u"Chat GPT", None))
        self.start_new.setText(QCoreApplication.translate("ChatGPT", u"Start New Chat", None))
    # retranslateUi

