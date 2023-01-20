import numpy

class Polynomfunctions():
    def __init__(self, basis, exponent, startwert):
        self.basis = basis
        self.exponent = exponent
        self.startwert = startwert

    def setStartwert(self, startwert):
        self.startwert = startwert

    def ableitenPolynom(self):
        newBasis = self.basis * self.exponent;
        newExponent = self.exponent - 1;

        if (self.exponent == 0):
            self.tangentenSteigung = str(0)
        elif (newExponent == 0):
            self.tangentenSteigung = str(newBasis)
        else:
            self.tangentenSteigung = str(newBasis)+"x^"+str(newExponent)
            return str(newBasis) + "x^ " + str(newExponent)

    def yAchsenabschnittBerechnenStartwert(self):
        achse = self.basis * (self.startwert ** self.exponent)
        self.achsenAbschnitt = achse
        return achse

    def steigungBerechnen(self):
        if (self.tangentenSteigung.__contains__("x^")):
            parts = self.tangentenSteigung.split("x^")
            self.tangentenSteigung = int(parts[0])*(self.startwert**int(parts[1]))
            return int(parts[0]) * (self.startwert**int(parts[1]))

    def yAchesnabschnittBerechnenTangente(self):
        tSteigungParts = self.tangentenSteigung.split("x^")
        newTangentenSteigung = int(tSteigungParts[0])*(self.startwert**int(tSteigungParts[1]))
        steigungNew = newTangentenSteigung*self.startwert
        self.achseTangente = self.achsenAbschnitt-steigungNew
        print("t(x)=" + str(newTangentenSteigung) + "x" + str(self.achseTangente))
        return self.achseTangente

    def getNewStartwert(self):
        newAchse = self.achseTangente * (-1)
        wert = newAchse / self.tangentenSteigung
        print(wert)
        return wert
