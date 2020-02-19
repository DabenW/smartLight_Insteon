# -*- coding: utf-8 -*-

#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import binascii
import time
from PyQt5.QtCore import *


class Runthread(QtCore.QThread):
    #  通过类成员对象定义信号对象
    _signal = pyqtSignal(str)

    def __init__(self):
        super(Runthread, self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            message = self.t.inWaiting()
            if message:
                data = str(binascii.b2a_hex(self.t.read(message)))[2:-1]
                if data.find('0250')>-1:
                    index = data.find('0250')+4
                    deviceID = data[index:index+6]
                    self._signal.emit(deviceID)
                    break
            # self._signal.emit(str(i))  # 注意这里与_signal = pyqtSignal(str)中的类型相同

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

        #set serial
        self.t = serial.Serial('com3', 19200)
        self.setSerial(self.t)

        #device set
        self.deviceSet = set()

        #light value
        self.lux = 0

        #bind button
        self.turnOn.clicked.connect(self.turnOnLight)
        self.turnOff.clicked.connect(self.turnOffLight)
        self.turnOnHalf.clicked.connect(self.turnOnHalfLight)
        self.link.clicked.connect(self.startlink)
        self.showUSBID.clicked.connect(self.getUSBID)
        self.lightSlider.valueChanged[int].connect(self.changeLight)

        self.setWindowOpacity(0.98)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setSerial(self,t):
        self.t = t

    def changeLight(self,value):
        self.lux = value
        self.turnOnHalf.setText("Turn On " + str(int((self.lux/15)*100)) + "% Light")

    def getUSBID(self):
        message = self.t.inWaiting()
        if message:
            self.t.read(message)
        d = bytes.fromhex('0260')
        self.t.write(d)
        time.sleep(0.5)
        message = self.t.inWaiting()

        if message:
            data = str(binascii.b2a_hex(self.t.read(message)))[2:-1]
            print(data)
            self.USBID.setText("USB comm: "+data[4:10])

    def startlink(self):
        d = bytes.fromhex('02 64 03 01')
        self.t.write(d)

        self.thread = Runthread()
        self.thread._signal.connect(self.call_backlog)
        self.thread.t = self.t
        self.thread.start()

    def call_backlog(self,deviceID):
        print("call back")
        if deviceID in self.deviceSet:
            pass
        else:
            self.listWidget.setStyleSheet("WidgetItem:pressed { background-color: #444444; }")
            self.deviceSet.add(deviceID)
            newItem = QtWidgets.QListWidgetItem()
            newItem.setText(deviceID)
            self.listWidget.insertItem(self.listWidget.count()+1,newItem)
            QtWidgets.QMessageBox.warning(self, "Confirming", "You connect to a new device "+deviceID,
                                          QtWidgets.QMessageBox.Ok)


    def turnOnLight(self):
        # self.t.open()
        if self.listWidget.currentItem():
            deviceid = self.listWidget.currentItem().text()
            d=bytes.fromhex('02 62 '+deviceid +' 0F 11 FF')
            self.t.write(d)
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please select one device or add one device", QtWidgets.QMessageBox.Ok)


    def turnOffLight(self):
        if self.listWidget.currentItem():
            deviceid = self.listWidget.currentItem().text()
            d=bytes.fromhex('02 62 '+deviceid+' 0F 13 00')
            self.t.write(d)
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please select one device or add one device", QtWidgets.QMessageBox.Ok)

    def turnOnHalfLight(self):
        if self.listWidget.currentItem():
            deviceid = self.listWidget.currentItem().text()
            chaDic = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
            lux = chaDic.get(self.lux,str(self.lux))
            print(lux)
            d=bytes.fromhex('02 62 '+deviceid+' 0F 11 '+str(lux)+'F')
            self.t.write(d)
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please select one device or add one device", QtWidgets.QMessageBox.Ok)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.turnOn.setText(_translate("MainWindow", "Turn On Light"))
        self.turnOff.setText(_translate("MainWindow", "Turn Off Light"))
        self.turnOnHalf.setText(_translate("MainWindow", "Turn On "+str(self.lux)+"% Light"))
        self.showUSBID.setText(_translate("MainWindow", "Show USB ID"))
        self.USBID.setText(_translate("MainWindow", "USB comm:"))
        self.link.setText(_translate("MainWindow", "Link"))
        self.Title.setText(_translate("MainWindow", "Dimmable device app"))
        self.min.setText(_translate("MainWindow", "Min"))
        self.max.setText(_translate("MainWindow", "Max"))