import pathlib
import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QWidget
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtUiTools import QUiLoader
from ui.mainwindow import Ui_MainWindow
from ui.chatWidget import Ui_chatWidget
from ui.chatComponent import Ui_chatComponent

class chatComponent(QWidget):
    def __init__(self, sender, message):
        super(chatComponent, self).__init__()
        self.ui = Ui_chatComponent()
        self.ui.setupUi(self)
        # uiFilePath = pathlib.Path(__file__).parent.joinpath('ui', 'chatComponent.ui')
        # self.ui = QUiLoader().load(uiFilePath.as_posix())
        # self.ui.setupUi(self)
        # self.setCentralWidget(self.ui)
        self.ui.l_sender.setText(sender)
        self.ui.te_message.setPlainText(message)
        self.ui.tb_delComponent.clicked.connect(self.delete)

    def delete(self):
        self.deleteLater()


class chatWidget(QWidget):
    def __init__(self):
        super(chatWidget, self).__init__()
        self.ui = Ui_chatWidget()
        self.ui.setupUi(self)

        messageList =[
            {
                'sender': 'taro.yamada',
                'message': 'レビューお願いします。'
            },
            {
                'sender': 'hanako.yamada',
                'message': 'とても良い感じです！！ありがとうございます！'
            }
        ]
        for i, message in enumerate(messageList):
            chatComponentInstance = chatComponent(messageList[i].get('sender'), messageList[i].get('message'))
            # self.ui.scrollArea.insert
            self.ui.verticalLayout_5.insertWidget(i, chatComponentInstance)

        # self.ui.tb_send.clicked.connect(chatComponentInstance.deleteLater())
        self.ui.tb_send.clicked.connect(self.addMessage)

    def addMessage(self):
        message = self.ui.te_editMessage.toPlainText()
        chatComponentInstance = chatComponent('hoge', message)
        self.ui.verticalLayout_5.addWidget(chatComponentInstance)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.verticalLayout_2.addWidget(chatWidget())

        



# def getMessagesJson(limit, date):
#     loadFilePath = pathlib.Path(__file__).parent.joinpath('messages.json')
#     if loadFilePath.exists():
#         with open(loadFilePath.as_posix(), mode="r") as f:
#             tempDict = json.load(f)
#         if list(tempDict.keys())[0] == date:
#             temp = tempDict.get(date)
    
#     return temp

def main():
    app = QApplication([])
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()