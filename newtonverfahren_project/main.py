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


def ableitenPolynom(basis, exponent):
    newBasis = basis*exponent;
    newExponent = exponent-1;

    if(exponent == 0):
        print(basis)
    else:
        print(str(newBasis)+"x^"+str(newExponent))

print(numpy.sin(numpy.deg2rad(2)))
ableitenPolynom(1, numpy.sin(numpy.deg2rad(2)))
