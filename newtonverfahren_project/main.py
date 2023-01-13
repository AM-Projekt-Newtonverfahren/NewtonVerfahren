import sys
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy
from PyQt5.QtWidgets import QApplication, QLabel


def app_test():
    app = QApplication([])
    label = QLabel("Hello world")
    label.show()
    app.exec_()


def ableitenPolynom(exponent):
    newBasis = exponent;
    newExponent = exponent-1;

    if(exponent == 0):
        print(0)
    else:
        print(str(newBasis)+"x^"+str(newExponent))

def ableitenExponent(basis):
    print(str(basis)+"^x*LOGe("+str(basis)+")")

#interpreter
def SteigungBerechnen(startwert, funktion):
    if(funktion.__contains__("x^")):
        pass

def yAchsenabschnittBerechnen(startwert, funktion):
    pass

ableitenPolynom(4)
ableitenExponent(3)
