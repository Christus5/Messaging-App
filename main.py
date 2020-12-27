from gui.window import Window
from PyQt5.QtWidgets import QApplication
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()

    win.show()
    app.aboutToQuit.connect(lambda: win.back_to_login())

    sys.exit(app.exec_())
