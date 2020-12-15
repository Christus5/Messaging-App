from gui.myApp import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow)
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.logOut.clicked.connect(self.back_to_login)
        self.ui.loginButton.clicked.connect(self.login_to_account)
        self.ui.createButton.clicked.connect(self.create_user)

        self.ui.sendButton.clicked.connect(self.send_message)

    def back_to_login(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def login_to_account(self):
        username = self.ui.inputUsername.text()
        password = self.ui.inputPassword.text()

        if username == "admin" and password == "admin":
            self.ui.inputPassword.setText('')
            self.ui.inputUsername.setText('')
            self.ui.stackedWidget.setCurrentIndex(1)
        else:
            print("incorrect login credentials!")

    def create_user(self):
        pass

    def send_message(self):
        print('message sent!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()

    win.show()
    sys.exit(app.exec_())
