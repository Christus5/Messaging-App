from gui.window import Window
from PyQt5.QtWidgets import QApplication
import sys
from PyQt5.QtMultimedia import QSound

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()

    win.show()
    app.aboutToQuit.connect(lambda: win.check_messages.terminate())

    sys.exit(app.exec_())
