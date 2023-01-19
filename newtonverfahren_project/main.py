import sys
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy
#from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QHBoxLayout, QScrollArea



"""def app_test():
    app = QApplication([])
    window = QWidget()
    layoutPrinciple = QHBoxLayout();
    scrollArea = QScrollArea()
    label = QLabel("Hello world")
    layoutPrinciple.addWidget(scrollArea)
    window.setLayout(layoutPrinciple)
    window.show()
    app.exec_()"""




#app_test()

function = Polynomfunctions()
ableitung = function.ableitenPolynom(2, 3)
achse = function.yAchsenabschnittBerechnenStartwert(1, 2, 3)
achseTangente = function.yAchesnabschnittBerechnenTangente(achse, 1, ableitung, 2, 3)
steigung = function.SteigungBerechnen(1, ableitung)
function.getNewStartwert(achseTangente, steigung)

