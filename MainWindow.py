# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(734, 424)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(734, 424))
        MainWindow.setMaximumSize(QtCore.QSize(734, 424))
        MainWindow.setBaseSize(QtCore.QSize(734, 424))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 122, 711, 281))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.begin_date = QtWidgets.QDateTimeEdit(self.gridLayoutWidget)
        self.begin_date.setObjectName("begin_date")
        self.gridLayout.addWidget(self.begin_date, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.end_date = QtWidgets.QDateTimeEdit(self.gridLayoutWidget)
        self.end_date.setObjectName("end_date")
        self.gridLayout.addWidget(self.end_date, 3, 1, 1, 1)
        self.browse_html = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browse_html.sizePolicy().hasHeightForWidth())
        self.browse_html.setSizePolicy(sizePolicy)
        self.browse_html.setMinimumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.browse_html.setFont(font)
        self.browse_html.setObjectName("browse_html")
        self.gridLayout.addWidget(self.browse_html, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.cert_status = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.cert_status.setMaximumSize(QtCore.QSize(600, 50))
        self.cert_status.setObjectName("cert_status")
        self.gridLayout.addWidget(self.cert_status, 7, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setMaximumSize(QtCore.QSize(300, 50))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.browse_cert = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.browse_cert.setMinimumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.browse_cert.setFont(font)
        self.browse_cert.setObjectName("browse_cert")
        self.gridLayout.addWidget(self.browse_cert, 7, 0, 1, 1)
        self.client_ip = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.client_ip.setObjectName("client_ip")
        self.gridLayout.addWidget(self.client_ip, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setMaximumSize(QtCore.QSize(300, 20))
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.server_ip = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.server_ip.setObjectName("server_ip")
        self.gridLayout.addWidget(self.server_ip, 0, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 391, 81))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.inter_status = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.inter_status.setObjectName("inter_status")
        self.gridLayout_4.addWidget(self.inter_status, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)
        self.db_status = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.db_status.setObjectName("db_status")
        self.gridLayout_4.addWidget(self.db_status, 1, 1, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(410, 10, 311, 81))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Пуль управления"))
        self.label_5.setText(_translate("MainWindow", "Начало периода"))
        self.browse_html.setText(_translate("MainWindow", "Отобразить страницу"))
        self.label_6.setText(_translate("MainWindow", "Конец периода"))
        self.label_3.setText(_translate("MainWindow", "IP адрес клиента"))
        self.browse_cert.setText(_translate("MainWindow", "Отобразить сертификат"))
        self.label_8.setText(_translate("MainWindow", "IP адрес сервера"))
        self.inter_status.setText(_translate("MainWindow", "Online"))
        self.label.setText(_translate("MainWindow", "Статус сервера"))
        self.label_4.setText(_translate("MainWindow", "Статус соединения с БД"))
        self.db_status.setText(_translate("MainWindow", "Online"))
