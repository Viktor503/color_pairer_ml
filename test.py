# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testing.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
        
import sys
import numpy as np
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        def change_backgr():
            MainWindow.setStyleSheet("background-color:rgb(%r,%g,%d)" %(self.horizontalSlider.value(),self.horizontalSlider_2.value(),self.horizontalSlider_3.value()))

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 190, 409, 116))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(60, 400, 160, 22))
        self.horizontalSlider.setMaximum(255)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(290, 400, 160, 22))
        self.horizontalSlider_2.setMaximum(255)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(520, 400, 160, 22))
        self.horizontalSlider_3.setMaximum(255)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 320, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 320, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(530, 320, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        font = QtGui.QFont()
        font.setPointSize(18)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.horizontalSlider.setValue(255)
        self.horizontalSlider_2.setValue(255)
        self.horizontalSlider_3.setValue(255)

        self.horizontalSlider.valueChanged.connect(change_backgr)
        self.horizontalSlider_2.valueChanged.connect(change_backgr)
        self.horizontalSlider_3.valueChanged.connect(change_backgr)

        MainWindow.setStyleSheet("background-color:rgb(%r,%g,%d)" %(self.horizontalSlider.value(),self.horizontalSlider_2.value(),self.horizontalSlider_3.value()))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def change_fontclr(self,r,g,b):
            self.label.setStyleSheet("color:rgb(%r,%g,%d)" %(r,g,b))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Project Pineapple"))
        self.label.setText(_translate("MainWindow", "Pineapple"))
        self.label_2.setText(_translate("MainWindow", "red"))
        self.label_3.setText(_translate("MainWindow", "green"))
        self.label_3.adjustSize()
        self.label_4.setText(_translate("MainWindow", "blue"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
