# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WidgetTourSchedule.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TourSchedForm(object):
    def setupUi(self, TourSchedForm):
        TourSchedForm.setObjectName("TourSchedForm")
        TourSchedForm.resize(391, 412)
        self.label_13 = QtWidgets.QLabel(TourSchedForm)
        self.label_13.setGeometry(QtCore.QRect(140, 10, 111, 21))
        self.label_13.setObjectName("label_13")
        self.performanceEdit = QtWidgets.QLineEdit(TourSchedForm)
        self.performanceEdit.setGeometry(QtCore.QRect(160, 40, 221, 20))
        self.performanceEdit.setObjectName("performanceEdit")
        self.startEdit = QtWidgets.QLineEdit(TourSchedForm)
        self.startEdit.setGeometry(QtCore.QRect(160, 70, 221, 20))
        self.startEdit.setObjectName("startEdit")
        self.endEdit = QtWidgets.QLineEdit(TourSchedForm)
        self.endEdit.setGeometry(QtCore.QRect(160, 100, 221, 20))
        self.endEdit.setObjectName("endEdit")
        self.locationEdit = QtWidgets.QLineEdit(TourSchedForm)
        self.locationEdit.setGeometry(QtCore.QRect(160, 240, 221, 20))
        self.locationEdit.setObjectName("locationEdit")
        self.err_msg = QtWidgets.QLabel(TourSchedForm)
        self.err_msg.setGeometry(QtCore.QRect(86, 300, 211, 20))
        self.err_msg.setText("")
        self.err_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.err_msg.setObjectName("err_msg")
        self.okButton = QtWidgets.QPushButton(TourSchedForm)
        self.okButton.setGeometry(QtCore.QRect(56, 350, 91, 23))
        self.okButton.setObjectName("okButton")
        self.cancelButton = QtWidgets.QPushButton(TourSchedForm)
        self.cancelButton.setGeometry(QtCore.QRect(240, 350, 91, 23))
        self.cancelButton.setObjectName("cancelButton")
        self.label = QtWidgets.QLabel(TourSchedForm)
        self.label.setGeometry(QtCore.QRect(70, 40, 91, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(TourSchedForm)
        self.label_2.setGeometry(QtCore.QRect(80, 70, 71, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(TourSchedForm)
        self.label_3.setGeometry(QtCore.QRect(60, 100, 91, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(TourSchedForm)
        self.label_4.setGeometry(QtCore.QRect(50, 130, 101, 21))
        self.label_4.setObjectName("label_4")
        self.addButton = QtWidgets.QPushButton(TourSchedForm)
        self.addButton.setGeometry(QtCore.QRect(180, 270, 75, 23))
        self.addButton.setObjectName("addButton")
        self.delButton = QtWidgets.QPushButton(TourSchedForm)
        self.delButton.setGeometry(QtCore.QRect(280, 270, 75, 23))
        self.delButton.setObjectName("delButton")
        self.listView = QtWidgets.QListView(TourSchedForm)
        self.listView.setGeometry(QtCore.QRect(160, 130, 221, 101))
        self.listView.setObjectName("listView")

        self.retranslateUi(TourSchedForm)
        QtCore.QMetaObject.connectSlotsByName(TourSchedForm)

    def retranslateUi(self, TourSchedForm):
        _translate = QtCore.QCoreApplication.translate
        TourSchedForm.setWindowTitle(_translate("TourSchedForm", "Tour schedule form"))
        self.label_13.setText(_translate("TourSchedForm", "Заполните данные"))
        self.okButton.setText(_translate("TourSchedForm", "OK"))
        self.cancelButton.setText(_translate("TourSchedForm", "Отмена"))
        self.label.setText(_translate("TourSchedForm", "Представление:"))
        self.label_2.setText(_translate("TourSchedForm", "Дата начала:"))
        self.label_3.setText(_translate("TourSchedForm", "Дата окончания:"))
        self.label_4.setText(_translate("TourSchedForm", "Места проведения:"))
        self.addButton.setText(_translate("TourSchedForm", "Добавить"))
        self.delButton.setText(_translate("TourSchedForm", "Удалить"))
