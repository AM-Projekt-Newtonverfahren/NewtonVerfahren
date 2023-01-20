from Polynomfunctions import *

class Newtonverfahren:
    def __init__(self):
        pass

    def polynomfunctions(self):
        if (function.__contains__("+")):
            functionBlocks = function.split("+")
        elif (function.__contains__("-")):
            functionBlocks = function.split("-")

    def potenzfunctions(self, function, startwert, repeat):
        functionParts = function.split("x^")
        potenzfunction = Polynomfunctions(int(functionParts[0]), int(functionParts[1]), startwert)

        for i in range(repeat):
            ableitung = potenzfunction.ableitenPolynom()
            achse = potenzfunction.yAchsenabschnittBerechnenStartwert()
            achseTangente = potenzfunction.yAchesnabschnittBerechnenTangente()
            steigung = potenzfunction.steigungBerechnen()
            newStartwert = potenzfunction.getNewStartwert()
            potenzfunction.setStartwert(newStartwert)
