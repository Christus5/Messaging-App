from gui.myApp import Ui_messagingApp
import time
from PyQt5.QtWidgets import (QMainWindow)
from PyQt5 import QtCore
from assets.classes.timing import Worker
from assets.data_base import (messages, users)
from assets.data_generator import generate_messages
from assets.classes.message import Message
from assets.classes.matplotlib_canvas import MplCanvas
import pandas as pd


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_messagingApp()
        self.ui.setupUi(self)

        "self properties"
        # current user
        self.user: str = ''

        # messages rendered for current user
        self.rendered_messages: list = []

        # check for new messages
        self.check_messages = Worker(self.rendered_messages)

        "initialization"
        # set starting indexes at 0
        self.reset_pages_tabs()

        # button actions
        self.init_button_actions()

        # background threads
        self.init_background_workers()

        self.chart_update()
        self.sc = MplCanvas(self)

        self.df = pd.DataFrame(self.rendered_messages)

    """
        Active methods (that can be called by users)
    """

    def chart_update(self):
        try:
            df = pd.DataFrame(self.rendered_messages)
            df = (df['sender'].groupby(df['sender'])).count()

            self.sc.axes.cla()

            df.plot(ax=self.sc.axes,
                    kind='pie',
                    autopct='%1.1f%%',
                    ylabel='')

            self.sc.draw()
            self.ui.chartsLayout.addWidget(self.sc)
        except KeyError:
            pass

    def back_to_login(self) -> None:
        # stop checking for new messages
        self.check_messages.terminate()

        # transfer user to login page
        self.ui.stackedWidget.setCurrentIndex(0)

    def login_to_account(self) -> None:
        # get inputs from user
        username = self.ui.inputUsername.text()
        password = self.ui.inputPassword.text()

        # give user visual response
        self.set_login_inputs('rgb(186, 189, 182)')

        user = users.find_one({"username": username, "password": password})
        if user:
            self.rendered_messages = []
            self.ui.messages.setText('')
            self.user = ''
            self.ui.inputPassword.setText('')
            self.ui.inputUsername.setText('')
            self.ui.stackedWidget.setCurrentIndex(1)
            self.user = username
            self.check_messages.update_rendered_messages(self.rendered_messages)
            self.check_messages.start()

            if self.user != 'admin':
                self.ui.admin_delete_messages.hide()
                self.ui.admin_generate_messages.hide()
            else:
                self.ui.admin_delete_messages.show()
                self.ui.admin_generate_messages.show()

            self.ui.loginResult.setText('')

        else:
            # give user visual response
            self.set_login_result("Incorrect login credentials!", 'red')
            self.set_login_inputs('red')

    def create_user(self) -> None:
        # get inputs from user
        username: str = self.ui.inputUsername.text()
        password: str = self.ui.inputPassword.text()

        # check for empty input values
        if username and password:
            # check if user exists
            if users.find_one({"username": username}):
                # give user visual response
                self.set_login_result("User already exists!", 'red')
                self.set_login_inputs('red')
            else:
                # create new user in mongodb
                users.insert_one({"username": username, "password": password})

                # give user visual response
                self.set_login_result("Successfully created!", 'green')
                self.set_login_inputs('green')
        else:
            # give user visual response
            self.set_login_result("Please fill all fields", 'red')
            self.set_login_inputs('red')

    def send_message(self) -> None:
        # get text from message input
        new_message = self.ui.messageInput.toPlainText()

        # clear message input
        self.ui.messageInput.setText("")

        # check for empty message input
        if new_message != '':
            messages.insert_one({"message": new_message, "id": -1, "sender": self.user, "date": time.asctime()})

    """ 
        Passive methods (that run in background) 
    """

    def render_message(self, message) -> None:
        # check if sender is user
        is_user = True if message['sender'] == self.user else False

        # create Message object
        new_message = Message(message['message'], message['sender'], message['date'], is_user)

        # insert messages to messages frame
        self.ui.messages.insertHtml(new_message.to_html())
        self.ui.messages.textCursor().insertBlock()

        # update rendered messages list
        self.rendered_messages.append(message)
        self.check_messages.update_rendered_messages(self.rendered_messages)
        # self.chart_update()

        # scrolls messages to bottom
        self.ui.messages.ensureCursorVisible()

    def set_login_result(self, text: str, color: str) -> None:
        self.ui.loginResult.setText(text)
        self.ui.loginResult.setStyleSheet(f'color: {color};')

    def set_login_inputs(self, color: str) -> None:
        self.ui.inputUsername.setStyleSheet(f'border-bottom-color: {color};')
        self.ui.inputPassword.setStyleSheet(f'border-bottom-color: {color};')

    """
        Admin functions
    """

    def delete_messages(self) -> None:
        messages.drop()
        print(len(self.rendered_messages))
        self.ui.messages.setText('')
        self.rendered_messages = []
        self.check_messages.update_rendered_messages(self.rendered_messages)

    def generate_messages(self) -> None:
        generate_messages(15)
        self.chart_update()

    """
        initialization
    """

    def init_button_actions(self):
        self.ui.logOut.clicked.connect(self.back_to_login)
        self.ui.loginButton.clicked.connect(self.login_to_account)

        # Enter-ის დაჭერით შედის მომხმარებელი
        self.ui.inputUsername.returnPressed.connect(self.login_to_account)
        self.ui.inputPassword.returnPressed.connect(self.login_to_account)
        
        self.ui.createButton.clicked.connect(self.create_user)
        self.ui.admin_delete_messages.clicked.connect(self.delete_messages)
        self.ui.admin_generate_messages.clicked.connect(self.generate_messages)
        self.ui.sendButton.clicked.connect(self.send_message)
        self.ui.refreshChart.clicked.connect(self.chart_update)

    def init_background_workers(self):
        self.check_messages.checkMessage.connect(self.render_message)

    def reset_pages_tabs(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.page_2_tabs.setCurrentIndex(0)
