# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ASF(object):
    def setupUi(self, ASF):
        ASF.setObjectName("ASF")
        ASF.resize(982, 592)
        self.centralwidget = QtWidgets.QWidget(ASF)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)
        self.comboBox_gost = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_gost.setObjectName("comboBox_gost")
        self.comboBox_gost.addItem("")
        self.comboBox_gost.addItem("")
        self.gridLayout.addWidget(self.comboBox_gost, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.comboBox_Dy = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_Dy.setObjectName("comboBox_Dy")
        self.comboBox_Dy.addItem("")
        self.comboBox_Dy.addItem("")
        self.comboBox_Dy.addItem("")
        self.comboBox_Dy.addItem("")
        self.comboBox_Dy.addItem("")
        self.comboBox_Dy.addItem("")
        self.comboBox_Dy.addItem("")
        self.comboBox_Dy.addItem("")
        self.comboBox_Dy.addItem("")
        self.comboBox_Dy.addItem("")
        self.comboBox_Dy.addItem("")
        self.comboBox_Dy.addItem("")
        self.comboBox_Dy.addItem("")
        self.comboBox_Dy.addItem("")
        self.comboBox_Dy.addItem("")
        self.comboBox_Dy.addItem("")
        self.comboBox_Dy.addItem("")
        self.comboBox_Dy.addItem("")
        self.comboBox_Dy.addItem("")
        self.comboBox_Dy.addItem("")
        self.comboBox_Dy.addItem("")
        self.comboBox_Dy.addItem("")
        self.gridLayout.addWidget(self.comboBox_Dy, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.spinBox_number = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_number.setObjectName("spinBox_number")
        self.gridLayout.addWidget(self.spinBox_number, 0, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.lineEdit_pipe = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_pipe.setObjectName("lineEdit_pipe")
        self.gridLayout.addWidget(self.lineEdit_pipe, 2, 3, 1, 1)
        self.comboBox_type = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_type.setObjectName("comboBox_type")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.gridLayout.addWidget(self.comboBox_type, 3, 1, 1, 1)
        self.lineEdit_pipe_length = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_pipe_length.setObjectName("lineEdit_pipe_length")
        self.gridLayout.addWidget(self.lineEdit_pipe_length, 1, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.comboBox_answer = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_answer.setObjectName("comboBox_answer")
        self.comboBox_answer.addItem("")
        self.comboBox_answer.addItem("")
        self.comboBox_answer.addItem("")
        self.gridLayout.addWidget(self.comboBox_answer, 4, 1, 1, 1)
        self.comboBox_pressure = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_pressure.setObjectName("comboBox_pressure")
        self.comboBox_pressure.addItem("")
        self.comboBox_pressure.addItem("")
        self.comboBox_pressure.addItem("")
        self.comboBox_pressure.addItem("")
        self.comboBox_pressure.addItem("")
        self.gridLayout.addWidget(self.comboBox_pressure, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 2, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_name.setObjectName("lineEdit_name")


        self.gridLayout.addWidget(self.lineEdit_name, 3, 3, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(168, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_Image = QtWidgets.QLabel(self.groupBox)
        self.label_Image.setObjectName("label_Image")
        self.horizontalLayout.addWidget(self.label_Image)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout_2.addWidget(self.pushButton_add)
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.horizontalLayout_2.addWidget(self.pushButton_delete)
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout_2.addWidget(self.pushButton_save)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(19)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(20, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(81)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.verticalLayout.addWidget(self.tableWidget)
        ASF.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ASF)
        self.statusbar.setObjectName("statusbar")
        ASF.setStatusBar(self.statusbar)

        self.retranslateUi(ASF)
        QtCore.QMetaObject.connectSlotsByName(ASF)

    def retranslateUi(self, ASF):
        _translate = QtCore.QCoreApplication.translate
        ASF.setWindowTitle(_translate("ASF", "Auto Selector Flange"))
        self.groupBox.setTitle(_translate("ASF", "Установите параметры"))
        self.label_7.setText(_translate("ASF", "Днина патрубка, мм"))
        self.comboBox_gost.setItemText(0, _translate("ASF", "12820 (плоский)"))
        self.comboBox_gost.setItemText(1, _translate("ASF", "12821 (сапожковый)"))
        self.label_2.setText(_translate("ASF", "Давление, Py"))
        self.label_3.setText(_translate("ASF", "Условный проход Dy"))
        self.comboBox_Dy.setItemText(0, _translate("ASF", "15"))
        self.comboBox_Dy.setItemText(1, _translate("ASF", "20"))
        self.comboBox_Dy.setItemText(2, _translate("ASF", "25"))
        self.comboBox_Dy.setItemText(3, _translate("ASF", "32"))
        self.comboBox_Dy.setItemText(4, _translate("ASF", "40"))
        self.comboBox_Dy.setItemText(5, _translate("ASF", "50"))
        self.comboBox_Dy.setItemText(6, _translate("ASF", "65"))
        self.comboBox_Dy.setItemText(7, _translate("ASF", "80"))
        self.comboBox_Dy.setItemText(8, _translate("ASF", "100"))
        self.comboBox_Dy.setItemText(9, _translate("ASF", "125"))
        self.comboBox_Dy.setItemText(10, _translate("ASF", "150"))
        self.comboBox_Dy.setItemText(11, _translate("ASF", "175"))
        self.comboBox_Dy.setItemText(12, _translate("ASF", "200"))
        self.comboBox_Dy.setItemText(13, _translate("ASF", "225"))
        self.comboBox_Dy.setItemText(14, _translate("ASF", "250"))
        self.comboBox_Dy.setItemText(15, _translate("ASF", "300"))
        self.comboBox_Dy.setItemText(16, _translate("ASF", "350"))
        self.comboBox_Dy.setItemText(17, _translate("ASF", "400"))
        self.comboBox_Dy.setItemText(18, _translate("ASF", "500"))
        self.comboBox_Dy.setItemText(19, _translate("ASF", "600"))
        self.comboBox_Dy.setItemText(20, _translate("ASF", "700"))
        self.comboBox_Dy.setItemText(21, _translate("ASF", "800"))
        self.label.setText(_translate("ASF", "Фланец ГОСТ"))
        self.label_6.setText(_translate("ASF", "Количество"))
        self.comboBox_type.setItemText(0, _translate("ASF", "1"))
        self.comboBox_type.setItemText(1, _translate("ASF", "2"))
        self.comboBox_type.setItemText(2, _translate("ASF", "3"))
        self.label_8.setText(_translate("ASF", "Труба"))
        self.label_5.setText(_translate("ASF", "Ответный/заглушка/Нет"))
        self.comboBox_answer.setItemText(0, _translate("ASF", "Заглушка"))
        self.comboBox_answer.setItemText(1, _translate("ASF", "Ответный"))
        self.comboBox_answer.setItemText(2, _translate("ASF", "Нет"))
        self.comboBox_pressure.setItemText(0, _translate("ASF", "0,1-0,25 МПа"))
        self.comboBox_pressure.setItemText(1, _translate("ASF", "0,6 МПа"))
        self.comboBox_pressure.setItemText(2, _translate("ASF", "1,0 МПа"))
        self.comboBox_pressure.setItemText(3, _translate("ASF", "1,6 МПа"))
        self.comboBox_pressure.setItemText(4, _translate("ASF", "2,5 МПа"))
        self.label_4.setText(_translate("ASF", "Тип фланца"))
        self.label_9.setText(_translate("ASF", "Обозначение"))
        self.label_Image.setText(_translate("ASF", "Image(soon...)"))
        self.pushButton_add.setText(_translate("ASF", "Добавить"))
        self.pushButton_delete.setText(_translate("ASF", "Удалить"))
        self.pushButton_save.setText(_translate("ASF", "Сохранить"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ASF", "Обозначение"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ASF", "Dy"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ASF", "Py"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ASF", "тип"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ASF", "масса"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("ASF", "диаметр"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("ASF", "толщина"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("ASF", "Ответный"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("ASF", "тип"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("ASF", "масса"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("ASF", "толщина"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("ASF", "кол-во"))

        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("ASF", "крепеж"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("ASF", "длина шпильки"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("ASF", "кол-во"))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("ASF", "шайбы кол-во"))

        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("ASF", "прокладка"))
        item = self.tableWidget.horizontalHeaderItem(17)
        item.setText(_translate("ASF", "кол-во"))
        item = self.tableWidget.horizontalHeaderItem(18)
        item.setText(_translate("ASF", "длина трубы"))
        self.tableWidget.resizeColumnsToContents()
        self.lineEdit_pipe.setText('20x2.5')