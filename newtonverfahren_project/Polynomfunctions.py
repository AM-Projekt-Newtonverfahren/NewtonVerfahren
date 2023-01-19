import numpy

class Polynomfunctions:
    def __init__(self):
        pass

    def ableitenPolynom(basis, exponent):
        newBasis = basis * exponent;
        newExponent = exponent - 1;

        if (exponent == 0):
            print(0)
        elif (newExponent == 0):
            print(str(newBasis))
        else:
            print(str(newBasis) + "x^ " + str(newExponent))
            return str(newBasis) + "x^ " + str(newExponent)

    def yAchsenabschnittBerechnenStartwert(startwert, basis, exponent):
        achse = basis * (startwert ** exponent)
        print(achse)
        return achse

    def yAchesnabschnittBerechnenTangente(yAchse, startwert, ableitung, basis, exponent):
        if (ableitung.__contains__("x^")):
            parts = ableitung.split("x^")
            function = basis * (startwert ** exponent)
            ableitungMitStartwert = int(parts[0]) * (startwert ** int(parts[1]))
            steigung = function - ableitungMitStartwert
            print(steigung)
            return steigung

    def ableitenExponent(basis):
        print(str(basis) + "^x*LOGe( " + str(basis) + ")")

    # TODO: interpreter
    def SteigungBerechnen(startwert, funktion):
        if (funktion.__contains__("x^")):
            parts = funktion.split("x^")
            return int(parts[0]) * (startwert ** int(parts[1]))

    def getNewStartwert(achse, steigung):
        newAchse = achse * (-1)
        wert = newAchse / steigung
        print(wert)
