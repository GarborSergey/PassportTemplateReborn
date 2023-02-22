import sys
from os import sep

from PyQt6 import *
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow

from mainwindow import Ui_MainWindow

VERSION = "0.0.0"


class PassportTemplate(QMainWindow):
    def __init__(self):
        super(PassportTemplate, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    root = PassportTemplate()
    root.show()
    sys.exit(app.exec())
