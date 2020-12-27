# gui
from gui import Ui_messagingApp

# PyQt5 imports
from PyQt5.QtWidgets import (QMainWindow, QListWidgetItem)
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QSound

# assets
from assets import (
    Worker,
    messages, users,
    generate_messages,
    Message,
    MplCanvas,
    Naming)

# other libraries
import pandas as pd
import time


class Window(QMainWindow, Ui_messagingApp):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)

        "self properties"
        # current user
        self.user: 'str' = ''

        self.activeUsersShow: 'bool' = True

        # messages rendered for current user
        self.rendered_messages: 'list' = []
        self.rendered_users: 'list' = []

        # check for new messages
        self.check_messages = Worker(self.rendered_messages)

        "initialization"
        # set starting indexes at 0
        self.reset_pages_tabs()

        # When user logins, this checks what message was sent lastly
        try:
            self.last_message = messages.find().sort(Naming.DATE, -1) \
                .limit(1).next()[Naming.DATE]
        except StopIteration:
            self.last_message = None

        # button actions
        self.init_button_actions()

        # event listener
        self.messageInput.installEventFilter(self)

        # background threads
        self.init_background_workers()

        self.chart_update()
        self.sc = MplCanvas(self)

        self.df = pd.DataFrame(self.rendered_messages)

    """
        Active methods (that can be called by users)
    """

    def chart_update(self) -> None:
        try:
            df = pd.DataFrame(self.rendered_messages)
            df = (df[Naming.SENDER].groupby(df[Naming.SENDER])).count()

            self.sc.axes.cla()

            df.plot(ax=self.sc.axes,
                    kind='pie',
                    autopct='%1.0f%%',
                    ylabel='',
                    title='Messages Share By User')

            self.sc.draw()
            self.chartsLayout.addWidget(self.sc)
        except KeyError:
            pass

    def back_to_login(self) -> None:
        # stop checking for new messages
        self.check_messages.terminate()

        # update user's state to offline in db
        users.update_one({Naming.USERNAME: self.user}, {'$set': {Naming.ACTIVE: False}})

        # clear active users pane;
        self.activeUsers.clear()
        self.rendered_users.clear()

        # transfer user to login page
        self.stackedWidget.setCurrentIndex(0)

    def login_to_account(self) -> None:
        # get inputs from user
        username = self.inputUsername.text()
        password = self.inputPassword.text()

        # give user visual response
        self.set_login_inputs('rgb(186, 189, 182)')

        user = users.find_one({Naming.USERNAME: username, Naming.PASSWORD: password})
        if user:
            QSound.play('assets/sounds/login.sound.wav')
            self.reset_values_for_login()
            self.user = username
            self.check_messages.update_rendered_messages(self.rendered_messages)
            self.check_messages.start()

            users.update_one(user, {'$set': {Naming.ACTIVE: True}})

            if self.user != 'admin':
                self.admin_delete_messages.hide()
                self.admin_generate_messages.hide()
            else:
                self.admin_delete_messages.show()
                self.admin_generate_messages.show()

            self.loginResult.setText('')

        else:
            # give user visual response
            self.set_login_result("Incorrect login credentials!", 'red')
            self.set_login_inputs('red')

    def create_user(self) -> None:
        # get inputs from user
        username: str = self.inputUsername.text()
        password: str = self.inputPassword.text()

        # check for empty input values
        if username and password:
            # check if user exists
            if users.find_one({Naming.USERNAME: username}):
                # give user visual response
                self.set_login_result("User already exists!", 'red')
                self.set_login_inputs('red')
            elif len(password) < 5:
                self.set_login_inputs('red')
                self.loginResult.setText("Password should contain at least "
                                         "5 characters")
                self.loginResult.setStyleSheet('color: red; font-size: 11px')

            else:
                QSound.play('assets/sounds/create.sound.wav')
                # create new user in mongodb
                users.insert_one({Naming.USERNAME: username, Naming.PASSWORD: password, Naming.ACTIVE: False})

                # give user visual response
                self.set_login_result("Successfully created!", 'green')
                self.set_login_inputs('green')
        else:
            # give user visual response
            self.set_login_result("Please fill all fields", 'red')
            self.set_login_inputs('red')

    def send_message(self) -> None:
        # get text from message input
        new_message = self.messageInput.toPlainText()

        # clear message input
        self.messageInput.setText("")

        # check for empty message input
        if new_message != '':
            messages.insert_one(
                {Naming.MESSAGE: new_message, "id": -1, Naming.SENDER: self.user,
                 Naming.DATE: time.asctime(), Naming.RTIME: time.time()})

            QSound.play('assets/sounds/sending_sound.wav')

    def toggle_active_users(self) -> None:
        self.activeUsersShow = not self.activeUsersShow
        self.activeUsersLabel.hide()
        y: 'int' = 170
        x: 'int' = 540
        self.activeUsersButton.setIcon(QIcon('assets/images/arrow_users.svg'))
        self.activeUsers.hide()

        if self.activeUsersShow:
            x = 300
            self.activeUsersLabel.show()
            self.render_active_users()
            self.activeUsersButton.setIcon(QIcon('assets/images/arrow_forward.svg'))
            self.activeUsers.show()

        self.activeUsersButton.move(x, y)

    """ 
        Passive methods (that run in background) 
    """

    def render_message(self, message) -> None:
        # check if sender is user
        is_user = True if message[Naming.SENDER] == self.user else False

        # create Message object
        new_message = Message(message[Naming.MESSAGE], message[Naming.SENDER],
                              message[Naming.DATE], message[Naming.RTIME], is_user)

        print(time.time(), new_message.rtime)
        if not is_user and (time.time() - new_message.rtime < 1.5):
            QSound.play('assets/sounds/receiving_sound.wav')

        # insert messages to messages frame
        self.messages.insertHtml(new_message.to_html())
        self.messages.textCursor().insertBlock()

        # update rendered messages list
        self.rendered_messages.append(message)

        # scrolls messages to bottom
        self.messages.ensureCursorVisible()

        # When rendering last message sent (during login), update chart
        if self.last_message and self.last_message == new_message.date:
            self.chart_update()

    def set_login_result(self, text: str, color: str) -> None:
        self.loginResult.setText(text)
        self.loginResult.setStyleSheet(f'color: {color};')

    def set_login_inputs(self, color: str) -> None:
        self.inputUsername.setStyleSheet(f'border-bottom-color: {color};')
        self.inputPassword.setStyleSheet(f'border-bottom-color: {color};')

    def render_active_users(self) -> None:
        active_users = list(users.find())

        for user in active_users:
            if user[Naming.ACTIVE] and user[Naming.USERNAME] not in self.rendered_users:
                self.rendered_users.append(user[Naming.USERNAME])

                item_wrapper = QListWidgetItem(user[Naming.USERNAME])
                self.activeUsers.addItem(item_wrapper)

    def eventFilter(self, obj: 'QObject', event: 'QEvent') -> bool:
        if event.type() == QtCore.QEvent.KeyPress and obj is self.messageInput:
            if event.key() == QtCore.Qt.Key_Return and self.messageInput.hasFocus():
                self.send_message()
                return True
        return super().eventFilter(obj, event)

    def reset_values_for_login(self):
        self.rendered_messages = []
        self.toggle_active_users()
        self.messages.setText('')
        self.inputPassword.setText('')
        self.inputUsername.setText('')
        self.stackedWidget.setCurrentIndex(1)

    """
        Admin functions
    """

    def delete_messages(self) -> None:
        messages.drop()
        print(len(self.rendered_messages))
        self.messages.clear()
        self.rendered_messages = []
        self.check_messages.update_rendered_messages(self.rendered_messages)

    def generate_messages(self) -> None:
        generate_messages(15)
        self.chart_update()

    """
        initialization
    """

    def init_button_actions(self) -> None:
        self.logOut.clicked.connect(self.back_to_login)
        self.loginButton.clicked.connect(self.login_to_account)

        # Enter-ის დაჭერით შედის მომხმარებელი
        self.inputUsername.returnPressed.connect(self.login_to_account)
        self.inputPassword.returnPressed.connect(self.login_to_account)

        self.createButton.clicked.connect(self.create_user)
        self.admin_delete_messages.clicked.connect(self.delete_messages)
        self.admin_generate_messages.clicked.connect(self.generate_messages)
        self.sendButton.clicked.connect(self.send_message)
        self.refreshChart.clicked.connect(self.chart_update)
        self.activeUsersButton.clicked.connect(self.toggle_active_users)

    def init_background_workers(self) -> None:
        self.check_messages.checkMessage.connect(self.render_message)

    def reset_pages_tabs(self) -> None:
        self.stackedWidget.setCurrentIndex(0)
        self.page_2_tabs.setCurrentIndex(0)
