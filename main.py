import sys
from PyQt5.QtWidgets import QApplication
from gui.window import Window


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()

    sys.exit(app.exec_())