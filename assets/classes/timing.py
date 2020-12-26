from PyQt5.QtCore import QThread, pyqtSignal
from assets.data_base import messages


class Worker(QThread):
    checkMessage = pyqtSignal(dict)

    def __init__(self, r_m,  parent=None):
        QThread.__init__(self, parent)
        self.running = False
        self.rendered_m = r_m

    def run(self):
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
