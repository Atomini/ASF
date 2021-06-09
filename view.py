import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from interface import Ui_ASF


class View:
    _current_position = 0

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
        """Подставляет рекомендуемое значение для трубы в поле ввода"""
        Dy = self.ui.comboBox_Dy.currentText()
        pipe = self.controller.recomend_pipe(Dy)
        self.ui.lineEdit_pipe.setText(pipe)

    def add_date_in_table(self, date):
        self.ui.tableWidget.insertRow(self._current_position)
        self.ui.tableWidget.setItem(self._current_position, 0, QTableWidgetItem(self.ui.lineEdit_name.text()))
        self.ui.tableWidget.setItem(self._current_position, 1, QTableWidgetItem(self.ui.comboBox_gost.currentText()[0:5]))
        self.ui.tableWidget.setItem(self._current_position, 2, QTableWidgetItem(str(date[0])))
        self.ui.tableWidget.setItem(self._current_position, 3, QTableWidgetItem(str(date[1])))
        self.ui.tableWidget.setItem(self._current_position, 4, QTableWidgetItem(self.ui.comboBox_type.currentText()))
        self.ui.tableWidget.setItem(self._current_position, 5, QTableWidgetItem(str(date[2])))
        self.ui.tableWidget.setItem(self._current_position, 6, QTableWidgetItem(str(date[3])))
        self.ui.tableWidget.setItem(self._current_position, 7, QTableWidgetItem(str(date[4])))
        self.ui.tableWidget.setItem(self._current_position, 8, QTableWidgetItem(self.ui.comboBox_answer.currentText()))
        self.ui.tableWidget.setItem(self._current_position, 9, QTableWidgetItem(str(date[6])))
        self.ui.tableWidget.setItem(self._current_position, 10, QTableWidgetItem(str(date[7])))
        self.ui.tableWidget.setItem(self._current_position, 11, QTableWidgetItem(str(date[8])))
        self.ui.tableWidget.setItem(self._current_position, 12, QTableWidgetItem(self.ui.spinBox_number.text()))
        self.ui.tableWidget.setItem(self._current_position, 13, QTableWidgetItem(str(date[9])))
        self.ui.tableWidget.setItem(self._current_position, 14, QTableWidgetItem(str(date[10])))
        self.ui.tableWidget.setItem(self._current_position, 15, QTableWidgetItem(str(date[11])))
        self.ui.tableWidget.setItem(self._current_position, 16, QTableWidgetItem(str(date[12])))
        self.ui.tableWidget.setItem(self._current_position, 17, QTableWidgetItem(str(date[12])))
        self.ui.tableWidget.setItem(self._current_position, 18, QTableWidgetItem(str(date[13])))
        self.ui.tableWidget.setItem(self._current_position, 19, QTableWidgetItem(str(date[14])))
        self.ui.tableWidget.setItem(self._current_position, 20, QTableWidgetItem(self.ui.lineEdit_pipe.text()))
        self.ui.tableWidget.setItem(self._current_position, 21, QTableWidgetItem(self.ui.lineEdit_pipe_length.text()))
        self._current_position += 1

    def delete_date_in_table(self):
        try:
            if self.ui.tableWidget.selectedRanges():
                index = self.ui.tableWidget.selectedRanges()
                index = index[0].bottomRow()
            else:
                index = self._current_position-1
            self.ui.tableWidget.removeRow(index)
            self._current_position -= 1
        except IndexError as error:
            print(error)

    def save_data_to_exel(self) -> list:
        """Возвращает список с параметрами из таблици"""
        data = []
        for i in range(0, self._current_position):
            data.append([])
            for j in range(0, 22):
                data[i].append(self.ui.tableWidget.item(i, j).text())
        return data

    # must be last
    def main(self):
        # срабативыет при изменении в комбобоксе
        self.ui.comboBox_Dy.activated[int].connect(self.set_recomend_pipe)
        # срабатывает при нажатии кнопки добавить
        self.ui.pushButton_add.clicked.connect(self.controller.add_button_click)
        # срабатывает при нажатии кнопки Удалить
        self.ui.pushButton_delete.clicked.connect(self.delete_date_in_table)
        # срабатывает при нажатии кнопки сохранить
        self.ui.pushButton_save.clicked.connect(self.controller.save_button_click)
        # must be last
        self.window.show()
        sys.exit(self.app.exec())
