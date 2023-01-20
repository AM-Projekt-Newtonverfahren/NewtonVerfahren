import numpy

class Polynomfunctions():
    def __init__(self, basis, exponent, startwert):
        self.basis = basis
        self.exponent = exponent
        self.startwert = startwert

    def ableitenPolynom(self):
        newBasis = self.basis * self.exponent;
        newExponent = self.exponent - 1;

        if (self.exponent == 0):
            print(0)
        elif (newExponent == 0):
            print(str(newBasis))
        else:
            print(str(newBasis) + "x^" + str(newExponent))
            self.tangentenSteigung = str(newBasis)+"x^"+str(newExponent)
            return str(newBasis) + "x^ " + str(newExponent)

    def yAchsenabschnittBerechnenStartwert(self):
        achse = self.basis * (self.startwert ** self.exponent)
        print(achse)
        self.achsenAbschnitt = achse
        return achse

    def yAchesnabschnittBerechnenTangente(self):
        if (self.tangentenSteigung.__contains__("x^")):
            parts = self.tangentenSteigung.split("x^")
            function = self.basis * (self.startwert ** self.exponent)
            ableitungMitStartwert = int(parts[0]) * (self.startwert ** int(parts[1]))
            steigung = function - ableitungMitStartwert
            print(steigung)
            self.achseTangente = steigung
            return steigung

    def steigungBerechnen(self):
        if (self.tangentenSteigung.__contains__("x^")):
            parts = self.tangentenSteigung.split("x^")
            self.tangentenSteigung = int(parts[0])*(self.startwert**int(parts[1]))
            return int(parts[0]) * (self.startwert ** int(parts[1]))

    def getNewStartwert(self):
        newAchse = self.achseTangente * (-1)
        wert = newAchse / self.tangentenSteigung
        print(wert)
