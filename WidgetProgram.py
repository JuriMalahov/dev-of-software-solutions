# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WidgetProgram.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProgramForm(object):
    def setupUi(self, ProgramForm):
        ProgramForm.setObjectName("ProgramForm")
        ProgramForm.resize(391, 431)
        self.err_msg = QtWidgets.QLabel(ProgramForm)
        self.err_msg.setGeometry(QtCore.QRect(90, 340, 211, 20))
        self.err_msg.setText("")
        self.err_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.err_msg.setObjectName("err_msg")
        self.okButton = QtWidgets.QPushButton(ProgramForm)
        self.okButton.setGeometry(QtCore.QRect(60, 380, 91, 23))
        self.okButton.setObjectName("okButton")
        self.cancelButton = QtWidgets.QPushButton(ProgramForm)
        self.cancelButton.setGeometry(QtCore.QRect(240, 380, 91, 23))
        self.cancelButton.setObjectName("cancelButton")
        self.label_3 = QtWidgets.QLabel(ProgramForm)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 111, 21))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(ProgramForm)
        self.label.setGeometry(QtCore.QRect(70, 40, 81, 21))
        self.label.setObjectName("label")
        self.label_13 = QtWidgets.QLabel(ProgramForm)
        self.label_13.setGeometry(QtCore.QRect(140, 10, 111, 21))
        self.label_13.setObjectName("label_13")
        self.label_4 = QtWidgets.QLabel(ProgramForm)
        self.label_4.setGeometry(QtCore.QRect(80, 130, 71, 21))
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(ProgramForm)
        self.label_2.setGeometry(QtCore.QRect(80, 70, 71, 21))
        self.label_2.setObjectName("label_2")
        self.priceEdit = QtWidgets.QLineEdit(ProgramForm)
        self.priceEdit.setGeometry(QtCore.QRect(160, 130, 221, 20))
        self.priceEdit.setObjectName("priceEdit")
        self.startdateEdit = QtWidgets.QLineEdit(ProgramForm)
        self.startdateEdit.setGeometry(QtCore.QRect(160, 70, 221, 20))
        self.startdateEdit.setObjectName("startdateEdit")
        self.performanceEdit = QtWidgets.QLineEdit(ProgramForm)
        self.performanceEdit.setGeometry(QtCore.QRect(160, 40, 221, 20))
        self.performanceEdit.setObjectName("performanceEdit")
        self.periodEdit = QtWidgets.QLineEdit(ProgramForm)
        self.periodEdit.setGeometry(QtCore.QRect(160, 100, 221, 20))
        self.periodEdit.setObjectName("periodEdit")
        self.addButton = QtWidgets.QPushButton(ProgramForm)
        self.addButton.setGeometry(QtCore.QRect(180, 300, 75, 23))
        self.addButton.setObjectName("addButton")
        self.label_5 = QtWidgets.QLabel(ProgramForm)
        self.label_5.setGeometry(QtCore.QRect(80, 160, 71, 21))
        self.label_5.setObjectName("label_5")
        self.daystimeEdit = QtWidgets.QLineEdit(ProgramForm)
        self.daystimeEdit.setGeometry(QtCore.QRect(160, 270, 221, 20))
        self.daystimeEdit.setObjectName("daystimeEdit")
        self.delButton = QtWidgets.QPushButton(ProgramForm)
        self.delButton.setGeometry(QtCore.QRect(280, 300, 75, 23))
        self.delButton.setObjectName("delButton")
        self.listView = QtWidgets.QListView(ProgramForm)
        self.listView.setGeometry(QtCore.QRect(160, 160, 221, 101))
        self.listView.setObjectName("listView")

        self.retranslateUi(ProgramForm)
        QtCore.QMetaObject.connectSlotsByName(ProgramForm)

    def retranslateUi(self, ProgramForm):
        _translate = QtCore.QCoreApplication.translate
        ProgramForm.setWindowTitle(_translate("ProgramForm", "Program form"))
        self.okButton.setText(_translate("ProgramForm", "OK"))
        self.cancelButton.setText(_translate("ProgramForm", "Отмена"))
        self.label_3.setText(_translate("ProgramForm", "Период проведения:"))
        self.label.setText(_translate("ProgramForm", "Представление:"))
        self.label_13.setText(_translate("ProgramForm", "Заполните данные"))
        self.label_4.setText(_translate("ProgramForm", "Цена билета:"))
        self.label_2.setText(_translate("ProgramForm", "Дата начала:"))
        self.addButton.setText(_translate("ProgramForm", "Добавить"))
        self.label_5.setText(_translate("ProgramForm", "Дни и время:"))
        self.delButton.setText(_translate("ProgramForm", "Удалить"))
