import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from interface import Ui_ASF


class View:

    def __init__(self, controller):
        self.controller = controller
        app = QApplication(sys.argv)
        window = QMainWindow()
        ui = Ui_ASF()
        ui.setupUi(window)
        window.show()
        sys.exit(app.exec())



