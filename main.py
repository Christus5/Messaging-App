from gui.myApp import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow)
import sys
import pymongo
import threading

ip = '192.168.0.108'
port = 27017
conn = pymongo.MongoClient(ip, port)
db = conn['messaging_app']
messages = db['messages']
users = db['users']


def set_interval(func, seconds: int = 1):
    def wrapper():
        func()
        set_interval(func)

    t = threading.Timer(seconds, wrapper)
    t.start()
    return t


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        self.user = None
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.logOut.clicked.connect(self.back_to_login)
        self.ui.loginButton.clicked.connect(self.login_to_account)
        self.ui.createButton.clicked.connect(self.create_user)

        self.ui.sendButton.clicked.connect(self.send_message)
        self.rendered_messages: list = []

    def back_to_login(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def login_to_account(self):
        username = self.ui.inputUsername.text()
        password = self.ui.inputPassword.text()

        user = users.find_one({ "username": username, "password": password })
        if user:
            self.ui.inputPassword.setText('')
            self.ui.inputUsername.setText('')
            self.ui.stackedWidget.setCurrentIndex(1)
            self.user = username
            set_interval(self.check_messages, seconds=1)
        else:
            print("incorrect login credentials!")

    def create_user(self):
        username: str = self.ui.inputUsername.text()
        password: str = self.ui.inputPassword.text()
        if username and password:
            if users.find_one({"username": username}):
                print("user already exists!")
            else:
                users.insert_one({"username": username, "password": password})

    def check_messages(self):
        for message in messages.find():
            if message not in self.rendered_messages:
                self.rendered_messages.append(message)
                new_message = str(f"{message['sender']}: {message['message']}")
                self.ui.messages.insertHtml(message['message'])

    def send_message(self):
        new_message = self.ui.messageInput.toPlainText()
        self.ui.messageInput.setText("")
        messages.insert_one({"message": new_message, "id": -1, "sender": self.user})


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()

    win.show()
    sys.exit(app.exec_())
