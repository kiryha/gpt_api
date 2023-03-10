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
        ChatGPT.resize(529, 905)
        self.centralwidget = QWidget(ChatGPT)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.layout = QVBoxLayout()
        self.layout.setObjectName(u"layout")

        self.verticalLayout.addLayout(self.layout)

        self.btn_test = QPushButton(self.centralwidget)
        self.btn_test.setObjectName(u"btn_test")

        self.verticalLayout.addWidget(self.btn_test)

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
        ChatGPT.setWindowTitle(QCoreApplication.translate("ChatGPT", u"MainWindow", None))
        self.btn_test.setText(QCoreApplication.translate("ChatGPT", u"PushButton", None))
    # retranslateUi

