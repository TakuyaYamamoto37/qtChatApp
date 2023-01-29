# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chatWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_chatWidget(object):
    def setupUi(self, chatWidget):
        if not chatWidget.objectName():
            chatWidget.setObjectName(u"chatWidget")
        chatWidget.resize(400, 396)
        self.verticalLayout = QVBoxLayout(chatWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea = QScrollArea(chatWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 378, 316))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.te_editMessage = QTextEdit(chatWidget)
        self.te_editMessage.setObjectName(u"te_editMessage")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.te_editMessage.sizePolicy().hasHeightForWidth())
        self.te_editMessage.setSizePolicy(sizePolicy)
        self.te_editMessage.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout.addWidget(self.te_editMessage)

        self.tb_send = QToolButton(chatWidget)
        self.tb_send.setObjectName(u"tb_send")
        self.tb_send.setMaximumSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.tb_send)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.verticalLayout_3)


        self.retranslateUi(chatWidget)

        QMetaObject.connectSlotsByName(chatWidget)
    # setupUi

    def retranslateUi(self, chatWidget):
        chatWidget.setWindowTitle(QCoreApplication.translate("chatWidget", u"Form", None))
        self.te_editMessage.setHtml(QCoreApplication.translate("chatWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Yu Gothic UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">testText</p></body></html>", None))
        self.tb_send.setText(QCoreApplication.translate("chatWidget", u"...", None))
    # retranslateUi

