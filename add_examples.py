# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys
import pandas as pd
from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        try:
            self.df = pd.read_excel("data.xlsx")
        except:
            self.df = pd.DataFrame(columns=['x1','x2','x3','y1','y2','y3','y4','y5','y6','y7','y8','y9','y10','y11','y12','y13','y14','y15','y16','y17','y18','y19','y20','y21','y22','y23','y24'])
        self.r1 = randint(0,255)
        self.r2 = randint(0,255)
        self.g1 = randint(0,255)
        self.g2 = randint(0,255)
        self.b1 = randint(0,255)
        self.b2 = randint(0,255)

        self.binr = list(format(self.r2,'08b'))
        self.bing = list(format(self.g2,'08b'))
        self.binb = list(format(self.b2,'08b'))

        #print(self.r2,self.g2,self.b2)
        #print(self.binr, self.bing, self.binb)
        
        def add_data():
            print("***************************************************************************")
            print(pd.DataFrame([[self.r1,self.g1,self.b1,self.r2,self.g2,self.b2]]))
            print("***************************************************************************")
            self.df = self.df.append({'x1':self.r1,'x2':self.g1,'x3':self.b1,'y1':self.binr[0], 'y2':self.binr[1], 'y3':self.binr[2], 'y4':self.binr[3], 'y5':self.binr[4], 'y6':self.binr[5], 'y7':self.binr[6], 'y8':self.binr[7], 'y9':self.bing[0], 'y10':self.bing[1], 'y11':self.bing[2], 'y12':self.bing[3], 'y13':self.bing[4], 'y14':self.bing[5], 'y15':self.bing[6], 'y16':self.bing[7], 'y17':self.binb[0], 'y18':self.binb[1], 'y19':self.binb[2], 'y20':self.binb[3], 'y21':self.binb[4], 'y22':self.binb[5], 'y23':self.binb[6], 'y24':self.binb[7]}, ignore_index=True)
            self.df.to_excel('data.xlsx', index=False)
            self.label2.setText(str(len(self.df.x1)))
            new_colors()
        def new_colors():
            self.r1 = randint(0,255)
            self.r2 = randint(0,255)
            self.g1 = randint(0,255)
            self.g2 = randint(0,255)
            self.b1 = randint(0,255)
            self.b2 = randint(0,255)
            self.binr = list(format(self.r2,'08b'))
            self.bing = list(format(self.g2,'08b'))
            self.binb = list(format(self.b2,'08b'))

            #print(self.r1,self.g1,self.b1)
            #print(self.r2,self.g2,self.b2)
            #print(self.binr, self.bing, self.binb)

            MainWindow.setStyleSheet("background-color:rgb(%r,%g,%d)" %(self.r1,self.g1,self.b1))
            self.label.setStyleSheet("color:rgb(%r,%g,%d)" %(self.r2,self.g2,self.b2))  
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color:rgb(%r,%g,%d)" %(self.r1,self.g1,self.b1))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 190, 409, 116))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color:rgb(%r,%g,%d)" %(self.r2,self.g2,self.b2))

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(0, 0, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label2.setFont(font)
        self.label2.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 470, 141, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(add_data)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 470, 141, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(new_colors)
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
        amount = len(self.df.x1)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Pineapple"))
        self.label2.setText(_translate("MainWindow", str(len(self.df.x1))))
        self.pushButton.setText(_translate("MainWindow", "Looks good"))
        self.pushButton_2.setText(_translate("MainWindow", "Not good"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

