import sys
from PyQt5 import QtWidgets
import numpy as np
import pandas as pd
import test
from Model import Model

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

model = Model(neurdim=[3,128,128,128,24])
model.LoadWeights()
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