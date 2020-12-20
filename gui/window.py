from gui.myApp import Ui_MainWindow
import time
from PyQt5.QtWidgets import (QMainWindow)
from assets.classes.timing import SetInterval
from assets.data_base import (messages, users)
from assets.data_generator import generate_messages
from assets.classes.message import Message


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        self.user: str = ''
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.page_2_tabs.setCurrentIndex(0)
        self.ui.logOut.clicked.connect(self.back_to_login)
        self.ui.loginButton.clicked.connect(self.login_to_account)
        self.ui.createButton.clicked.connect(self.create_user)
        self.ui.admin_delete_messages.clicked.connect(self.delete_messages)
        self.cm = SetInterval()

        self.ui.sendButton.clicked.connect(self.send_message)
        self.rendered_messages: list = []

        # self.generate_messages_wrapper()

    def generate_messages_wrapper(self):
        # self.cm.terminate()
        generate_messages(100)
        # self.cm.call(self.check_messages, seconds=0.1)

    def back_to_login(self):
        self.cm.terminate()
        self.ui.stackedWidget.setCurrentIndex(0)

    def login_to_account(self):
        username = self.ui.inputUsername.text()
        password = self.ui.inputPassword.text()
        self.ui.inputUsername.setStyleSheet('border-bottom-color: rgb(186, 189, 182);')
        self.ui.inputPassword.setStyleSheet('border-bottom-color: rgb(186, 189, 182);')

        user = users.find_one({"username": username, "password": password})
        if user:
            self.rendered_messages = []
            self.ui.messages.setText('')
            self.user = ''
            self.ui.inputPassword.setText('')
            self.ui.inputUsername.setText('')
            self.ui.stackedWidget.setCurrentIndex(1)
            self.user = username
            self.cm.call(self.check_messages, seconds=0.1)
            # set_interval(self.check_messages, seconds=1)
            if self.user != 'admin':
                self.ui.admin_delete_messages.hide()
            else:
                self.ui.admin_delete_messages.show()
        else:
            self.ui.inputUsername.setStyleSheet('border-bottom-color: red;')
            self.ui.inputPassword.setStyleSheet('border-bottom-color: red;')
            print("incorrect login credentials!")

    def create_user(self):
        username: str = self.ui.inputUsername.text()
        password: str = self.ui.inputPassword.text()
        if username and password:
            if users.find_one({"username": username}):
                print("user already exists!")
                self.ui.inputUsername.setStyleSheet('border-bottom-color: red;')
                self.ui.inputPassword.setStyleSheet('border-bottom-color: red;')
            else:
                users.insert_one({"username": username, "password": password})
                self.ui.inputUsername.setStyleSheet('border-bottom-color: green;')
                self.ui.inputPassword.setStyleSheet('border-bottom-color: green;')
        else:
            self.ui.inputUsername.setStyleSheet('border-bottom-color: red;')
            self.ui.inputPassword.setStyleSheet('border-bottom-color: red;')

    def render_message(self, message):
        is_user = True if message['sender'] == self.user else False

        new_message = Message(message['message'], message['sender'], message['date'], is_user)

        self.ui.messages.insertHtml(new_message.to_html())
        self.ui.messages.textCursor().insertBlock()
        self.rendered_messages.append(message)

    def check_messages(self):
        for message in messages.find():
            if message not in self.rendered_messages:
                self.render_message(message)

    def send_message(self):
        new_message = self.ui.messageInput.toPlainText()
        self.ui.messageInput.setText("")
        if new_message != '':
            messages.insert_one({"message": new_message, "id": -1, "sender": self.user, "date": time.asctime()})

    def delete_messages(self):
        messages.drop()
        self.ui.messages.setText('')
        self.rendered_messages = []
