from gui.window import Window
from PyQt5.QtWidgets import QApplication
import sys
from assets.data_base import messages

if __name__ == '__main__':
    app = QApplication(sys.argv)
    messages.drop()
    win = Window()

    win.show()
    app.aboutToQuit.connect(lambda: win.cm.terminate())

    sys.exit(app.exec_())
