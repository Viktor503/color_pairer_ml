import sys
from PyQt5 import QtWidgets
import numpy as np
import pandas as pd
import add_examples
import test
from Model import Model


#ask for preffered collor pairs
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui1 = add_examples.Ui_MainWindow()
ui1.setupUi(MainWindow)
MainWindow.show()
app.exec()

if app.aboutToQuit:
    df = pd.read_excel("data.xlsx")
    x = np.array([df["x1"],df["x2"],df["x3"]])
    y = np.array([df["y1"],df["y2"],df["y3"],df["y4"],df["y5"],df["y6"],df["y7"],df["y8"],df["y9"],df["y10"],df["y11"],df["y12"],df["y13"],df["y14"],df["y15"],df["y16"],df["y17"],df["y18"],df["y19"],df["y20"],df["y21"],df["y22"],df["y23"],df["y24"]])
    dim = [3,128,128,128,24]
    model = Model(x,y,dim)
    model.train()
    model.SaveWeights()

ui = test.Ui_MainWindow()
ui.setupUi(MainWindow)

def changetextcolor():
    hyp = model.predict(np.array([[ui.horizontalSlider.value(),ui.horizontalSlider_2.value(),ui.horizontalSlider_3.value()]]).T)
    hyp = (hyp>=0.5)*1   
    result = "".join(str(x) for x in hyp).replace("[","").replace("]","")
    r = int(result[:8],2)
    g = int(result[8:16],2)
    b = int(result[16:],2)
    ui.change_fontclr(r,g,b)


ui.horizontalSlider.valueChanged.connect(changetextcolor)
ui.horizontalSlider_2.valueChanged.connect(changetextcolor)
ui.horizontalSlider_3.valueChanged.connect(changetextcolor)
MainWindow.show()
sys.exit(app.exec_())
