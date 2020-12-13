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
        self.ui.backButton.clicked.connect(self.back_to_login)
        self.ui.loginButton.clicked.connect(self.login_to_messages)

    def back_to_login(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def login_to_messages(self):
        self.ui.stackedWidget.setCurrentIndex(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()

    win.show()
    sys.exit(app.exec_())
