# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WidgetWorker.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WorkerForm(object):
    def setupUi(self, WorkerForm):
        WorkerForm.setObjectName("WorkerForm")
        WorkerForm.resize(391, 513)
        self.surnameEdit = QtWidgets.QLineEdit(WorkerForm)
        self.surnameEdit.setGeometry(QtCore.QRect(160, 40, 221, 20))
        self.surnameEdit.setObjectName("surnameEdit")
        self.nameEdit = QtWidgets.QLineEdit(WorkerForm)
        self.nameEdit.setGeometry(QtCore.QRect(160, 70, 221, 20))
        self.nameEdit.setObjectName("nameEdit")
        self.label = QtWidgets.QLabel(WorkerForm)
        self.label.setGeometry(QtCore.QRect(100, 40, 51, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(WorkerForm)
        self.label_2.setGeometry(QtCore.QRect(130, 70, 31, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(WorkerForm)
        self.label_3.setGeometry(QtCore.QRect(100, 100, 51, 21))
        self.label_3.setObjectName("label_3")
        self.patronymicEdit = QtWidgets.QLineEdit(WorkerForm)
        self.patronymicEdit.setGeometry(QtCore.QRect(160, 100, 221, 20))
        self.patronymicEdit.setObjectName("patronymicEdit")
        self.birthyearEdit = QtWidgets.QLineEdit(WorkerForm)
        self.birthyearEdit.setGeometry(QtCore.QRect(160, 130, 221, 20))
        self.birthyearEdit.setObjectName("birthyearEdit")
        self.admissionyearEdit = QtWidgets.QLineEdit(WorkerForm)
        self.admissionyearEdit.setGeometry(QtCore.QRect(160, 160, 221, 20))
        self.admissionyearEdit.setObjectName("admissionyearEdit")
        self.workexperienceEdit = QtWidgets.QLineEdit(WorkerForm)
        self.workexperienceEdit.setGeometry(QtCore.QRect(160, 190, 221, 20))
        self.workexperienceEdit.setObjectName("workexperienceEdit")
        self.postEdit = QtWidgets.QLineEdit(WorkerForm)
        self.postEdit.setGeometry(QtCore.QRect(160, 220, 221, 20))
        self.postEdit.setObjectName("postEdit")
        self.addressEdit = QtWidgets.QLineEdit(WorkerForm)
        self.addressEdit.setGeometry(QtCore.QRect(160, 280, 221, 20))
        self.addressEdit.setObjectName("addressEdit")
        self.cityEdit = QtWidgets.QLineEdit(WorkerForm)
        self.cityEdit.setGeometry(QtCore.QRect(160, 310, 221, 20))
        self.cityEdit.setObjectName("cityEdit")
        self.phoneEdit = QtWidgets.QLineEdit(WorkerForm)
        self.phoneEdit.setGeometry(QtCore.QRect(160, 340, 221, 20))
        self.phoneEdit.setObjectName("phoneEdit")
        self.performanceEdit = QtWidgets.QLineEdit(WorkerForm)
        self.performanceEdit.setGeometry(QtCore.QRect(160, 370, 221, 20))
        self.performanceEdit.setObjectName("performanceEdit")
        self.label_4 = QtWidgets.QLabel(WorkerForm)
        self.label_4.setGeometry(QtCore.QRect(80, 130, 81, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(WorkerForm)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 151, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(WorkerForm)
        self.label_6.setGeometry(QtCore.QRect(120, 190, 47, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(WorkerForm)
        self.label_7.setGeometry(QtCore.QRect(90, 220, 61, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(WorkerForm)
        self.label_8.setGeometry(QtCore.QRect(130, 250, 41, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(WorkerForm)
        self.label_9.setGeometry(QtCore.QRect(120, 280, 41, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(WorkerForm)
        self.label_10.setGeometry(QtCore.QRect(120, 310, 41, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(WorkerForm)
        self.label_11.setGeometry(QtCore.QRect(110, 340, 51, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(WorkerForm)
        self.label_12.setGeometry(QtCore.QRect(70, 370, 81, 21))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(WorkerForm)
        self.label_13.setGeometry(QtCore.QRect(140, 10, 111, 21))
        self.label_13.setObjectName("label_13")
        self.okButton = QtWidgets.QPushButton(WorkerForm)
        self.okButton.setGeometry(QtCore.QRect(60, 460, 91, 23))
        self.okButton.setObjectName("okButton")
        self.cancelButton = QtWidgets.QPushButton(WorkerForm)
        self.cancelButton.setGeometry(QtCore.QRect(240, 460, 91, 23))
        self.cancelButton.setObjectName("cancelButton")
        self.gender1 = QtWidgets.QRadioButton(WorkerForm)
        self.gender1.setGeometry(QtCore.QRect(180, 250, 82, 21))
        self.gender1.setObjectName("gender1")
        self.gender2 = QtWidgets.QRadioButton(WorkerForm)
        self.gender2.setGeometry(QtCore.QRect(280, 250, 82, 21))
        self.gender2.setObjectName("gender2")
        self.err_msg = QtWidgets.QLabel(WorkerForm)
        self.err_msg.setGeometry(QtCore.QRect(90, 420, 211, 20))
        self.err_msg.setText("")
        self.err_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.err_msg.setObjectName("err_msg")

        self.retranslateUi(WorkerForm)
        QtCore.QMetaObject.connectSlotsByName(WorkerForm)

    def retranslateUi(self, WorkerForm):
        _translate = QtCore.QCoreApplication.translate
        WorkerForm.setWindowTitle(_translate("WorkerForm", "Worker form"))
        self.label.setText(_translate("WorkerForm", "Фамилия:"))
        self.label_2.setText(_translate("WorkerForm", "Имя:"))
        self.label_3.setText(_translate("WorkerForm", "Отчество:"))
        self.label_4.setText(_translate("WorkerForm", "Год рождения:"))
        self.label_5.setText(_translate("WorkerForm", "Год поступления на работу:"))
        self.label_6.setText(_translate("WorkerForm", "Стаж:"))
        self.label_7.setText(_translate("WorkerForm", "Должность:"))
        self.label_8.setText(_translate("WorkerForm", "Пол:"))
        self.label_9.setText(_translate("WorkerForm", "Адрес:"))
        self.label_10.setText(_translate("WorkerForm", "Город:"))
        self.label_11.setText(_translate("WorkerForm", "Телефон:"))
        self.label_12.setText(_translate("WorkerForm", "Представление:"))
        self.label_13.setText(_translate("WorkerForm", "Заполните данные"))
        self.okButton.setText(_translate("WorkerForm", "ОК"))
        self.cancelButton.setText(_translate("WorkerForm", "Отмена"))
        self.gender1.setText(_translate("WorkerForm", "мужской"))
        self.gender2.setText(_translate("WorkerForm", "женский"))
