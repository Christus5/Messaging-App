# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myApp.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_messagingApp(object):
    def setupUi(self, messagingApp):
        messagingApp.setObjectName("messagingApp")
        messagingApp.resize(600, 500)
        messagingApp.setMinimumSize(QtCore.QSize(600, 500))
        messagingApp.setMaximumSize(QtCore.QSize(600, 500))
        messagingApp.setStyleSheet("/* default */\n"
"*{\n"
"    font-family: Helvetica;\n"
"    font-weight: bold;\n"
"    font-size: 12pt;\n"
"    border: 0;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 0;\n"
"    background-color: rgb(17, 132, 224);\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background: transparent;\n"
"    border: 0 ;\n"
"    border-bottom: 1px solid rgb(186, 189, 182);\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"/* end of default */\n"
"\n"
"#page_login {\n"
"    border-image: url(\'assets/images/bck.jpg\') 0 0 0 0 stretch stretch;    \n"
"}\n"
"\n"
"/* tab bar styles */\n"
"\n"
"QTabWidget::pane {\n"
"    border-top: 2px solid #C2C7CB;\n"
"}\n"
"\n"
"QTabBar {\n"
"    background-color: #C2C7CB;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: #0F0F0F;\n"
"    color: white;\n"
"    width: 196px;\n"
"    border-bottom-color: #C2C7CB;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: rgb(17, 132, 224);\n"
"}\n"
"QTabBar::tab:selected {\n"
"    border-bottom-color: #C2C7CB;\n"
"    outline: none;\n"
"}\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px;\n"
"}\n"
"\n"
"/* end of tab bar */\n"
"/* settings tab */\n"
"\n"
"#account_tab {\n"
"    background-color: white;\n"
"}\n"
"\n"
"Line {\n"
"    color: black;\n"
"    background-color: black;\n"
"}\n"
"\n"
"/* end of settings tab*/\n"
"\n"
"/* charts tab */\n"
"\n"
"#charts_tab {\n"
"    background-color: white;\n"
"}\n"
"\n"
"/* end of charts tab*/\n"
"#messages_tab {\n"
"    background-color: rgb(211, 215, 207)\n"
"}\n"
"\n"
"#loginWrapper {\n"
"    background-color: rgba(0, 0, 0, 0.7);\n"
"    border: 0;\n"
"}\n"
"\n"
"#loginHeader{\n"
"    color: rgb(17, 132, 224);\n"
"    font-size: 22pt;\n"
"}\n"
"\n"
"#createButton {\n"
"    background-color: rgb(65, 208, 124);\n"
"}\n"
"\n"
"#loginButton {\n"
"    background-color: rgb(17, 132, 224);\n"
"}\n"
"\n"
"#backButton {\n"
"    border: 0;\n"
"}\n"
"\n"
"#admin_delete_messages {\n"
"    background-color: rgb(204, 0, 0);\n"
"}\n"
"\n"
"#admin_generate_messages {\n"
"    background-color: rgb(65, 208, 124);\n"
"}\n"
"\n"
"/* messages tab */\n"
"\n"
"#sendButton {\n"
"    background-color: rgb(17, 132, 224);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"#sendButton:hover {\n"
"    background-color: rgb(107, 159, 255);\n"
"}\n"
"\n"
"#messages {\n"
"    border: 0;\n"
"    background-color: white;\n"
"}\n"
"\n"
"#activeUsers {\n"
"    padding-top: 50px;\n"
"    padding-left: 10px;\n"
"    background-color: rgb(243, 243, 243);\n"
"}\n"
"\n"
"#activeUsersButton {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#activeUsersButton:focus{\n"
"    outline: none;\n"
"}\n"
"\n"
"#messageInput {\n"
"    border: 0px solid;\n"
"}\n"
"\n"
"/* end of messages tab */\n"
"\n"
"\n"
"#logOut {\n"
"    background-color: rgb(239, 41, 41);\n"
"}\n"
"\n"
"/* drop down */\n"
"\n"
"QComboBox {\n"
"    background-color: rgba(0, 0, 0, 0.3);\n"
"    min-width: 6em;\n"
"    height: 1em;\n"
"    border: 0;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: rgba(0, 0, 0, 0.7);\n"
"}\n"
"\n"
"QComboBox::item {\n"
"    background-color: rgba(0, 0, 0, 0.2)\n"
"}\n"
"\n"
"QComboBox::item:checked {\n"
"    background-color: rgba(17, 132, 224, 0.4);\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(assets/images/arrow_down.png);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: 0;\n"
" }\n"
"\n"
"\n"
"/* end of drop down */\n"
"\n"
"/* scroll bar */\n"
"\n"
"QScrollBar:vertical {\n"
"    background: transparent;\n"
"    border: 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: rgba(0, 0, 0, 0.4);\n"
"    border: 0;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    background-color: 0;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    background-color: 0;\n"
"}\n"
"\n"
"/* end of scroll bar */\n"
"\n"
"")
        messagingApp.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(messagingApp)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-10, 0, 611, 501))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_login = QtWidgets.QWidget()
        self.page_login.setObjectName("page_login")
        self.loginWrapper = QtWidgets.QFrame(self.page_login)
        self.loginWrapper.setGeometry(QtCore.QRect(150, 80, 351, 341))
        self.loginWrapper.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.loginWrapper.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loginWrapper.setFrameShadow(QtWidgets.QFrame.Plain)
        self.loginWrapper.setObjectName("loginWrapper")
        self.loginButton = QtWidgets.QPushButton(self.loginWrapper)
        self.loginButton.setGeometry(QtCore.QRect(220, 290, 89, 25))
        self.loginButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginButton.setObjectName("loginButton")
        self.inputUsername = QtWidgets.QLineEdit(self.loginWrapper)
        self.inputUsername.setGeometry(QtCore.QRect(40, 130, 270, 25))
        self.inputUsername.setStyleSheet("")
        self.inputUsername.setObjectName("inputUsername")
        self.inputPassword = QtWidgets.QLineEdit(self.loginWrapper)
        self.inputPassword.setGeometry(QtCore.QRect(40, 210, 270, 25))
        self.inputPassword.setMouseTracking(True)
        self.inputPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputPassword.setClearButtonEnabled(False)
        self.inputPassword.setObjectName("inputPassword")
        self.createButton = QtWidgets.QPushButton(self.loginWrapper)
        self.createButton.setGeometry(QtCore.QRect(40, 290, 89, 25))
        self.createButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.createButton.setObjectName("createButton")
        self.loginHeader = QtWidgets.QLabel(self.loginWrapper)
        self.loginHeader.setGeometry(QtCore.QRect(46, 50, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.loginHeader.setFont(font)
        self.loginHeader.setTextFormat(QtCore.Qt.AutoText)
        self.loginHeader.setScaledContents(True)
        self.loginHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.loginHeader.setObjectName("loginHeader")
        self.loginResult = QtWidgets.QLabel(self.loginWrapper)
        self.loginResult.setGeometry(QtCore.QRect(46, 260, 261, 20))
        self.loginResult.setText("")
        self.loginResult.setAlignment(QtCore.Qt.AlignCenter)
        self.loginResult.setObjectName("loginResult")
        self.stackedWidget.addWidget(self.page_login)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.page_2_tabs = QtWidgets.QTabWidget(self.page_2)
        self.page_2_tabs.setGeometry(QtCore.QRect(10, 0, 600, 500))
        self.page_2_tabs.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.page_2_tabs.setAutoFillBackground(False)
        self.page_2_tabs.setTabPosition(QtWidgets.QTabWidget.North)
        self.page_2_tabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.page_2_tabs.setDocumentMode(False)
        self.page_2_tabs.setTabsClosable(False)
        self.page_2_tabs.setObjectName("page_2_tabs")
        self.messages_tab = QtWidgets.QWidget()
        self.messages_tab.setObjectName("messages_tab")
        self.messageInput = QtWidgets.QTextEdit(self.messages_tab)
        self.messageInput.setGeometry(QtCore.QRect(10, 430, 481, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.messageInput.setFont(font)
        self.messageInput.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.messageInput.setStyleSheet("")
        self.messageInput.setObjectName("messageInput")
        self.sendButton = QtWidgets.QPushButton(self.messages_tab)
        self.sendButton.setGeometry(QtCore.QRect(500, 430, 91, 31))
        self.sendButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/outline_send_black_18dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sendButton.setIcon(icon)
        self.sendButton.setAutoDefault(False)
        self.sendButton.setObjectName("sendButton")
        self.messages = QtWidgets.QTextEdit(self.messages_tab)
        self.messages.setEnabled(True)
        self.messages.setGeometry(QtCore.QRect(0, 0, 600, 421))
        self.messages.setAccessibleName("")
        self.messages.setAccessibleDescription("")
        self.messages.setReadOnly(True)
        self.messages.setObjectName("messages")
        self.activeUsersButton = QtWidgets.QPushButton(self.messages_tab)
        self.activeUsersButton.setGeometry(QtCore.QRect(540, 180, 51, 51))
        self.activeUsersButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.activeUsersButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/arrow_back_ios_new-black-18dp.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.activeUsersButton.setIcon(icon1)
        self.activeUsersButton.setObjectName("activeUsersButton")
        self.activeUsers = QtWidgets.QListWidget(self.messages_tab)
        self.activeUsers.setGeometry(QtCore.QRect(340, 1, 256, 421))
        self.activeUsers.setObjectName("activeUsers")
        self.activeUsersLabel = QtWidgets.QLabel(self.messages_tab)
        self.activeUsersLabel.setGeometry(QtCore.QRect(380, 10, 161, 20))
        self.activeUsersLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.activeUsersLabel.setObjectName("activeUsersLabel")
        self.page_2_tabs.addTab(self.messages_tab, "")
        self.charts_tab = QtWidgets.QWidget()
        self.charts_tab.setObjectName("charts_tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.charts_tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 581, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.chartsLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.chartsLayout.setContentsMargins(0, 0, 0, 0)
        self.chartsLayout.setObjectName("chartsLayout")
        self.admin_delete_messages = QtWidgets.QPushButton(self.charts_tab)
        self.admin_delete_messages.setGeometry(QtCore.QRect(10, 430, 161, 25))
        self.admin_delete_messages.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.admin_delete_messages.setObjectName("admin_delete_messages")
        self.admin_generate_messages = QtWidgets.QPushButton(self.charts_tab)
        self.admin_generate_messages.setGeometry(QtCore.QRect(410, 430, 181, 25))
        self.admin_generate_messages.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.admin_generate_messages.setObjectName("admin_generate_messages")
        self.refreshChart = QtWidgets.QPushButton(self.charts_tab)
        self.refreshChart.setGeometry(QtCore.QRect(410, 380, 181, 25))
        self.refreshChart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.refreshChart.setObjectName("refreshChart")
        self.page_2_tabs.addTab(self.charts_tab, "")
        self.account_tab = QtWidgets.QWidget()
        self.account_tab.setObjectName("account_tab")
        self.frame = QtWidgets.QFrame(self.account_tab)
        self.frame.setGeometry(QtCore.QRect(20, 20, 561, 431))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 6, 111, 21))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(20, 40, 138, 31))
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setEditable(False)
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(10, 30, 151, 2))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.save_button = QtWidgets.QPushButton(self.frame)
        self.save_button.setGeometry(QtCore.QRect(450, 390, 89, 25))
        self.save_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save_button.setObjectName("save_button")
        self.logOut = QtWidgets.QPushButton(self.frame)
        self.logOut.setGeometry(QtCore.QRect(20, 390, 89, 25))
        self.logOut.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logOut.setObjectName("logOut")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 101, 17))
        self.label_2.setObjectName("label_2")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(10, 130, 151, 2))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.color_selector = QtWidgets.QComboBox(self.frame)
        self.color_selector.setGeometry(QtCore.QRect(20, 140, 138, 31))
        self.color_selector.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.color_selector.setFrame(True)
        self.color_selector.setObjectName("color_selector")
        self.color_selector.addItem("")
        self.page_2_tabs.addTab(self.account_tab, "")
        self.stackedWidget.addWidget(self.page_2)
        messagingApp.setCentralWidget(self.centralwidget)
        self.actionLog_Iyt = QtWidgets.QAction(messagingApp)
        self.actionLog_Iyt.setObjectName("actionLog_Iyt")
        self.actionEdit = QtWidgets.QAction(messagingApp)
        self.actionEdit.setObjectName("actionEdit")
        self.actionEN = QtWidgets.QAction(messagingApp)
        self.actionEN.setObjectName("actionEN")
        self.actionKA = QtWidgets.QAction(messagingApp)
        self.actionKA.setObjectName("actionKA")
        self.actionEdit_2 = QtWidgets.QAction(messagingApp)
        self.actionEdit_2.setObjectName("actionEdit_2")
        self.actionLog_Put = QtWidgets.QAction(messagingApp)
        self.actionLog_Put.setObjectName("actionLog_Put")
        self.actionKA_2 = QtWidgets.QAction(messagingApp)
        self.actionKA_2.setObjectName("actionKA_2")
        self.actionED = QtWidgets.QAction(messagingApp)
        self.actionED.setObjectName("actionED")

        self.retranslateUi(messagingApp)
        self.stackedWidget.setCurrentIndex(1)
        self.page_2_tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(messagingApp)

    def retranslateUi(self, messagingApp):
        _translate = QtCore.QCoreApplication.translate
        messagingApp.setWindowTitle(_translate("messagingApp", "Messaging App"))
        self.loginButton.setText(_translate("messagingApp", "Login"))
        self.inputUsername.setPlaceholderText(_translate("messagingApp", "username"))
        self.inputPassword.setPlaceholderText(_translate("messagingApp", "password"))
        self.createButton.setText(_translate("messagingApp", "Create"))
        self.loginHeader.setText(_translate("messagingApp", "Login"))
        self.sendButton.setText(_translate("messagingApp", "Send"))
        self.sendButton.setShortcut(_translate("messagingApp", "Return"))
        self.messages.setHtml(_translate("messagingApp", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Helvetica\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.activeUsersLabel.setText(_translate("messagingApp", "Active Users"))
        self.page_2_tabs.setTabText(self.page_2_tabs.indexOf(self.messages_tab), _translate("messagingApp", "Messages"))
        self.admin_delete_messages.setText(_translate("messagingApp", "Delete Messages"))
        self.admin_generate_messages.setText(_translate("messagingApp", "Generate Messages"))
        self.refreshChart.setText(_translate("messagingApp", "Refresh Chart"))
        self.page_2_tabs.setTabText(self.page_2_tabs.indexOf(self.charts_tab), _translate("messagingApp", "Charts"))
        self.label.setText(_translate("messagingApp", "Language"))
        self.comboBox.setItemText(0, _translate("messagingApp", "English"))
        self.comboBox.setItemText(1, _translate("messagingApp", "ქართული"))
        self.save_button.setText(_translate("messagingApp", "Save"))
        self.logOut.setText(_translate("messagingApp", "Log Out"))
        self.label_2.setText(_translate("messagingApp", "User color"))
        self.color_selector.setItemText(0, _translate("messagingApp", "Select Color"))
        self.page_2_tabs.setTabText(self.page_2_tabs.indexOf(self.account_tab), _translate("messagingApp", "Account"))
        self.actionLog_Iyt.setText(_translate("messagingApp", "Log out"))
        self.actionEdit.setText(_translate("messagingApp", "Edit"))
        self.actionEN.setText(_translate("messagingApp", "EN"))
        self.actionKA.setText(_translate("messagingApp", "KA"))
        self.actionEdit_2.setText(_translate("messagingApp", "Edit"))
        self.actionLog_Put.setText(_translate("messagingApp", "Log Out"))
        self.actionKA_2.setText(_translate("messagingApp", "KA"))
        self.actionED.setText(_translate("messagingApp", "EN"))