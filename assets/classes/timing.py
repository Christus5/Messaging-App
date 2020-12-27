from PyQt5.QtCore import (QThread, pyqtSignal)
from assets.data_base import (messages, users)
import time


class Worker(QThread):
    checkMessage = pyqtSignal(dict)

    def __init__(self, r_m,  parent=None):
        QThread.__init__(self, parent)
        self.running = False
        self.rendered_m = r_m

    def run(self) -> None:
        self.running = True
        while self.running:
            for message in messages.find():
                if message not in self.rendered_m:
                    self.rendered_m.append(message)
                    self.checkMessage.emit(message)

    def terminate(self) -> None:
        self.running = False

    def update_rendered_messages(self, r_m) -> None:
        self.rendered_m = r_m


class CheckUsers(QThread):
    update_users = pyqtSignal()

    def __init__(self, existing_users: 'list', parent=None):
        QThread.__init__(self, parent)
        self.running = False
        self.e_u: 'list' = existing_users

    def run(self) -> None:
        self.running = True
        while self.running:
            time.sleep(1)
            if self.e_u != list(users.find()):
                self.e_u = list(users.find())
                self.update_users.emit()