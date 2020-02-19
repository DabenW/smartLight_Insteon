# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'smartUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.turnOn = QtWidgets.QPushButton(self.centralwidget)
        self.turnOn.setGeometry(QtCore.QRect(150, 460, 121, 31))
        self.turnOn.setObjectName("turnOn")
        self.turnOff = QtWidgets.QPushButton(self.centralwidget)
        self.turnOff.setGeometry(QtCore.QRect(320, 460, 111, 31))
        self.turnOff.setObjectName("turnOff")
        self.turnOnHalf = QtWidgets.QPushButton(self.centralwidget)
        self.turnOnHalf.setGeometry(QtCore.QRect(480, 460, 151, 31))
        self.turnOnHalf.setObjectName("turnOnHalf")
        self.showUSBID = QtWidgets.QPushButton(self.centralwidget)
        self.showUSBID.setGeometry(QtCore.QRect(150, 110, 111, 21))
        self.showUSBID.setObjectName("showUSBID")
        self.USBID = QtWidgets.QLabel(self.centralwidget)
        self.USBID.setGeometry(QtCore.QRect(310, 110, 171, 21))
        self.USBID.setObjectName("USBID")
        self.link = QtWidgets.QPushButton(self.centralwidget)
        self.link.setGeometry(QtCore.QRect(540, 270, 75, 24))
        self.link.setObjectName("link")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(230, 20, 361, 61))
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(150, 180, 341, 241))
        self.listWidget.setObjectName("listWidget")
        self.lightSlider = QtWidgets.QSlider(self.centralwidget)
        self.lightSlider.setGeometry(QtCore.QRect(190, 510, 401, 21))
        self.lightSlider.setMaximum(15)
        self.lightSlider.setPageStep(2)
        self.lightSlider.setOrientation(QtCore.Qt.Horizontal)
        self.lightSlider.setObjectName("lightSlider")
        self.min = QtWidgets.QLabel(self.centralwidget)
        self.min.setGeometry(QtCore.QRect(150, 510, 31, 16))
        self.min.setObjectName("min")
        self.max = QtWidgets.QLabel(self.centralwidget)
        self.max.setGeometry(QtCore.QRect(600, 510, 31, 16))
        self.max.setObjectName("max")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.turnOn.setText(_translate("MainWindow", "Turn On Light"))
        self.turnOff.setText(_translate("MainWindow", "Turn Off Light"))
        self.turnOnHalf.setText(_translate("MainWindow", "Turn On 50% Light"))
        self.showUSBID.setText(_translate("MainWindow", "Show USB ID"))
        self.USBID.setText(_translate("MainWindow", "USB comm:"))
        self.link.setText(_translate("MainWindow", "Link"))
        self.Title.setText(_translate("MainWindow", "Dimmable device app"))
        self.min.setText(_translate("MainWindow", "Min"))
        self.max.setText(_translate("MainWindow", "Max"))
