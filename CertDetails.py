# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CertDetails.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.info = QtWidgets.QTextBrowser(Form)
        self.info.setGeometry(QtCore.QRect(10, 10, 381, 281))
        self.info.setObjectName("info")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Детальная информация"))
