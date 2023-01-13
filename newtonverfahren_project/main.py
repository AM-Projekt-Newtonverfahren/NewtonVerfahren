import sys
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QHBoxLayout, QScrollArea



def app_test():
    app = QApplication([])
    window = QWidget()
    layoutPrinciple = QHBoxLayout();
    scrollArea = QScrollArea()
    label = QLabel("Hello world")
    layoutPrinciple.addWidget(scrollArea)
    window.setLayout(layoutPrinciple)
    window.show()
    app.exec_()

def ableitenPolynom(basis, exponent):
    newBasis = basis*exponent;
    newExponent = exponent-1;

    if(exponent == 0):
        print(0)
    else:
        print(str(newBasis)+"x^"+str(newExponent))

def yAchsenabschnittBerechnen(startwert, basis, exponent):
    achse = (basis*startwert)**exponent
    print(achse)
    
def ableitenExponent(basis):
    print(str(basis)+"^x*LOGe("+str(basis)+")")

#interpreter
def SteigungBerechnen(startwert, funktion):
    if(funktion.__contains__("x^")):
        pass


app_test()
ableitenPolynom(2, 1)
yAchsenabschnittBerechnen(1, 2, 3)
