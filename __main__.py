import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from homeGUI import *
import serial
from QssLoader import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        qssStyle = QssLoader.loadQss('style.qss')
        self.setStyleSheet(qssStyle)




def run():
    app = QApplication(sys.argv)
    myWin = MyWindow()
    palette1 = QPalette()
    palette1.setColor(myWin.backgroundRole(), QColor(238,242,242))   # 设置背景颜色
    myWin.setPalette(palette1)
    myWin.setWindowIcon(QIcon('icon.png'))
    myWin.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()