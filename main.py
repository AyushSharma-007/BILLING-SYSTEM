from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import random as rn
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 70, 81, 31))
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 500, 151, 31))
        self.pushButton.setObjectName("pushButton")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 110, 113, 22))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 110, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(420, 110, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 70, 81, 31))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(440, 70, 81, 31))
        self.label_3.setObjectName("label_3")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(570, 50, 31, 491))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 140, 581, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(610, 500, 151, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(10, 500, 131, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        current_datetime = datetime.now()
        qt_datetime = QtCore.QDateTime(current_datetime.year, current_datetime.month, current_datetime.day,
                                       current_datetime.hour, current_datetime.minute, current_datetime.second)

        self.dateTimeEdit.setDateTime(qt_datetime)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 210, 511, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("MOVIE-1")
        self.comboBox.addItem("MOVIE-2")
        self.comboBox.addItem("MOVIE-3")
        self.comboBox.addItem("MOVIE-4")

        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(200, 260, 42, 22))
        self.spinBox.setObjectName("spinBox")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(220, 0, 361, 41))
        self.label_5.setStyleSheet("font: 75 20pt 'MS Shell Dlg 2';")
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(640, 80, 71, 41))
        self.label_6.setStyleSheet("font: 75 20pt 'MS Shell Dlg 2';")
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 330, 141, 41))
        self.label_7.setStyleSheet("font: 10pt 'MS Shell Dlg 2';")
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(170, 160, 271, 41))
        self.label_8.setStyleSheet("font: 75 20pt 'MS Shell Dlg 2';")
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 250, 121, 41))
        self.label_9.setStyleSheet("font: 10pt 'MS Shell Dlg 2';")
        self.label_9.setObjectName("label_9")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(190, 340, 113, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(600, 140, 181, 341))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(20, 0, 91, 51))
        self.lcdNumber.setObjectName("lcdNumber")
        r = rn.randint(1,1000)
        self.lcdNumber.display(r)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.label.setText(_translate("MainWindow", "   NAME"))
        self.pushButton.setText(_translate("MainWindow", "SUBMIT"))
        self.label_2.setText(_translate("MainWindow", "PHONE NO"))
        self.label_3.setText(_translate("MainWindow", "BILL NO"))
        self.pushButton_2.setText(_translate("MainWindow", "PRINT"))
        self.label_5.setText(_translate("MainWindow", "MOVIE BILLING SYSTEM"))
        self.label_6.setText(_translate("MainWindow", "BILL"))
        self.label_7.setText(_translate("MainWindow", "PRICE PER TICKET"))
        self.label_8.setText(_translate("MainWindow", "MOVIE SELECTOR"))
        self.label_9.setText(_translate("MainWindow", "NO OF TICKET"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
