# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chatComponent.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QPlainTextEdit, QSizePolicy, QToolButton,
    QVBoxLayout, QWidget)

class Ui_chatComponent(object):
    def setupUi(self, chatComponent):
        if not chatComponent.objectName():
            chatComponent.setObjectName(u"chatComponent")
        chatComponent.setEnabled(True)
        chatComponent.resize(380, 112)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(chatComponent.sizePolicy().hasHeightForWidth())
        chatComponent.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(chatComponent)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.l_sender = QLabel(chatComponent)
        self.l_sender.setObjectName(u"l_sender")

        self.verticalLayout.addWidget(self.l_sender)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.te_message = QPlainTextEdit(chatComponent)
        self.te_message.setObjectName(u"te_message")
        self.te_message.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.te_message.sizePolicy().hasHeightForWidth())
        self.te_message.setSizePolicy(sizePolicy1)
        self.te_message.setMaximumSize(QSize(16777215, 70))
        self.te_message.setFrameShape(QFrame.NoFrame)
        self.te_message.setFrameShadow(QFrame.Sunken)
        self.te_message.setReadOnly(True)

        self.horizontalLayout.addWidget(self.te_message)

        self.tb_delComponent = QToolButton(chatComponent)
        self.tb_delComponent.setObjectName(u"tb_delComponent")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tb_delComponent.sizePolicy().hasHeightForWidth())
        self.tb_delComponent.setSizePolicy(sizePolicy2)
        self.tb_delComponent.setMaximumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.tb_delComponent)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(chatComponent)

        QMetaObject.connectSlotsByName(chatComponent)
    # setupUi

    def retranslateUi(self, chatComponent):
        chatComponent.setWindowTitle(QCoreApplication.translate("chatComponent", u"Form", None))
        self.l_sender.setText(QCoreApplication.translate("chatComponent", u"TextLabel", None))
        self.tb_delComponent.setText(QCoreApplication.translate("chatComponent", u"...", None))
    # retranslateUi

