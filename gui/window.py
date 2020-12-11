from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from gui.naming import *


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle("Messaging App")
        self.pages = {
            login: self.create_login_page(),
            messages: self.create_messages_page()
        }
        self.active_page = None
        self.set_active_page(login)
        self.init_login_ui()
        self.init_messages_ui()

    def set_active_page(self, name: str):
        self.active_page = self.pages[name]
        self.pages[login][inputs]['username'].hide()

        for page in self.pages.keys():
            print(f"Page: {page}")
            if name != page:
                print(f"\tTo be removed: {page}")
                for widgets in self.pages[page].keys():
                    print(f"\t\tWidgets: {widgets}")
                    for widget in self.pages[page][widgets].keys():
                        self.pages[page][widgets][widget].hide()
            else:
                print(f"\tPage to be Shown: {page}")
                for widgets in self.pages[page].keys():
                    print(f"\t\tWidgets: {widgets}")
                    for widget in self.pages[page][widgets].keys():
                        self.pages[page][widgets][widget].show()

    def init_login_ui(self):
        page = self.pages[login]
        # აქ როგორც გინდა ისე დაწერე, მე page[buttons] მირჩევნია
        btns = page[buttons]
        btns['login'].move(200, 250)
        btns['login'].setText("Login")
        btns['login'].clicked.connect(lambda: self.set_active_page(messages))

        page[inputs]['username'].move(200, 150)
        page[inputs]['password'].move(200, 200)

        for name in page[inputs].keys():
            page[inputs][name].setStyleSheet('background-color: #531034; color: #FFF;')

    def init_messages_ui(self):
        page = self.pages[messages]

        page[display]['main'].setGeometry(10, 10, 200, 200)
        page[display]['main'].setStyleSheet('background-color: #808080')

        page[inputs]['main'].setGeometry(10, 220, 150, 30)

        page[buttons]['send'].setText("Send")
        page[buttons]['send'].setGeometry(160, 220, 50, 30)

    def create_login_page(self):
        return {
            buttons: {
                'login': QtWidgets.QPushButton(self)
            },
            inputs: {
                'username': QtWidgets.QTextEdit(self),
                'password': QtWidgets.QTextEdit(self)
            },
            labels: {
                'username': QtWidgets.QLabel(self),
                'password': QtWidgets.QLabel(self)
            }
        }

    def create_messages_page(self):
        return {
            display: {
                'main': QtWidgets.QLabel(self)
            },
            inputs: {
                'main': QtWidgets.QTextEdit(self)
            },
            buttons: {
                'send': QtWidgets.QPushButton(self)
            }
        }
