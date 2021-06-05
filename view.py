import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from interface import Ui_ASF


class View:

    def __init__(self, controller):
        self.controller = controller
        self.app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.ui = Ui_ASF()
        self.ui.setupUi(self.window)

    def current_select(self):
        """Возвращает текущее значение выборов в окне"""
        gost = self.ui.comboBox_gost.currentText()
        pressure = self.ui.comboBox_pressure.currentText()
        Dy = self.ui.comboBox_Dy.currentText()
        flange_type = self.ui.comboBox_type.currentText()
        answer_flange = self.ui.comboBox_answer.currentText()
        number = self.ui.spinBox_number.value()
        pipe_length = self.ui.lineEdit_pipe_length.text()
        pipe = self.ui.lineEdit_pipe.text()
        name = self.ui.lineEdit_name.text()
        return gost, pressure, Dy, flange_type, answer_flange, number, pipe_length, pipe, name

    def set_recomend_pipe(self):
        Dy = self.ui.comboBox_Dy.currentText()
        pipe = self.controller.recomend_pipe(Dy)
        self.ui.lineEdit_pipe.setText(pipe)

    # must be last
    def main(self):
        self.ui.comboBox_Dy.activated[int].connect(self.set_recomend_pipe)
        self.ui.pushButton_add.clicked.connect(self.controller.add_button_click)
        self.window.show()
        sys.exit(self.app.exec())
