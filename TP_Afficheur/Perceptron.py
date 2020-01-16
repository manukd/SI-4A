import numpy
import csv
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self, nbInput, nbEpochs, learningRate, filename):
        self.nbInput = nbInput
        self.nbEpochs = nbEpochs
        self.learningRate = learningRate
        self.wTab = numpy.zeros((7, 4), dtype=float)
        self.biais = 1
        self.wBiais = numpy.zeros((4, 1), dtype=float)
        self.filenameCSV = filename
        self.wHistory = numpy.append(numpy.ravel(self.wTab), self.wBiais)
        self.compt = 0
        self.errorTab = numpy.zeros((self.nbEpochs, 1), dtype=float)

    def predict(self, input, indice):
        calc = input[0] * self.wTab[0][indice] + input[1] * self.wTab[1][indice] + input[2] * self.wTab[2][indice] + input[3] * self.wTab[3][indice] + input[4] * self.wTab[4][indice] + input[5] * self.wTab[5][indice] + input[6] * self.wTab[6][indice] + self.biais * self.wBiais[indice]
        if(calc > 0):
            res = calc
        else:
            res = 0
        return res

    def readWeight(self):
        with (open(self.filenameCSV)) as csvfile:
            line_count = 0
            read = csv.reader(csvfile, delimiter=';')
            for row in read:
                if line_count <= self.nbInput:
                    self.wTab[line_count - 1] = float(row[1])
                    line_count += 1

    def converge(self):
        temp = numpy.append(numpy.ravel(self.wTab), self.wBiais)
        if(temp == self.wHistory).all():
            self.compt += 1
        else:
            self.compt = 0
        self.wHistory = temp

    def convertB(self, tab):
        res = 0
        for i in range(len(tab)):
            res += pow(2, tab[i])
        return res

    def convertB2(self, tab):
        res = 0
        for i in range(len(tab)):
            res += pow(2, tab[0][i])
        return res

    def train(self, listInput, listeOutput):
        """while self.compt < 5:"""
        print(self.wTab)
        for k in range(self.nbEpochs):
            totalError = 0
            for i in range(10):
                for j in range(7):
                    for l in range(4):
                        predic = self.predict(listInput[i], l)
                        self.wTab[j][l] = self.wTab[j][l] + self.learningRate * (listeOutput[i][l] - predic) * listInput[i][j]
                        self.wBiais[l] = self.wBiais[l] + self.learningRate * (listeOutput[i][l] - predic) * self.biais
                """totalError += (1/2) * pow((predic - listeOutput[i]), 2)"""
            """self.errorTab[k] = totalError
            self.converge()
        plt.plot(self.errorTab)
        plt.show()"""
