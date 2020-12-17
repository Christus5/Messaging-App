from gui.window import Window
from PyQt5.QtWidgets import QApplication
import sys
import threading

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()

    win.show()
    app.aboutToQuit.connect(lambda: win.cm.terminate())

    sys.exit(app.exec_())
