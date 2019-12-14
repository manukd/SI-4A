import numpy
import csv
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self, nbInput, nbEpochs, learningRate, filename):
        self.nbInput = nbInput
        self.nbEpochs = nbEpochs
        self.learningRate = learningRate
        self.wTab = numpy.zeros((2, 1), dtype=float)
        self.biais = 1
        self.wBiais = 0
        self.filenameCSV = filename
        self.wHistory = numpy.append(numpy.ravel(self.wTab), self.wBiais)
        self.compt = 0
        self.errorTab = numpy.zeros((self.nbEpochs, 1), dtype=float)

    def predict(self, input1, input2):
        calc = input1 * self.wTab[0] + input2 * self.wTab[1] + self.biais * self.wBiais
        if(calc > 0):
            return 1
        else:
            return 0

    def writeWeight(self):
        file = open(self.filenameCSV, 'w', newline='')
        write = csv.writer(file, delimiter=';')
        write.writerow(('Name_Weight', 'Weight'))
        for a in range(2):
            write.writerow((a,self.wTab[a]))
        write.writerow(('Biais', self.wBiais))
        file.close()

    def readWeight(self):
        with (open(self.filenameCSV)) as csvfile:
            line_count = 0
            read = csv.reader(csvfile, delimiter=';')
            for row in read:
                if line_count == 1 + self.nbInput:
                    self.wBiais = float(row[1])
                if line_count != 0 and row[0] != '' and line_count <= self.nbInput:
                    self.wTab[line_count - 1] = float(row[1])
                    line_count += 1
                else:
                    line_count += 1


    def converge(self):
        temp = numpy.append(numpy.ravel(self.wTab), self.wBiais)
        if(temp == self.wHistory).all():
            self.compt += 1
        else:
            self.compt = 0
        self.wHistory = temp

    def train(self, listInput, listeOutput):
        self.readWeight()
        print(self.wTab)
        print(self.wBiais)
        """while self.compt < 5:"""
        for k in range(self.nbEpochs):
            totalError = 0
            for i in range(4):
                predic = self.predict(listInput[i][0], listInput[i][1])
                self.wTab[0] = self.wTab[0] + self.learningRate * (listeOutput[i] - predic) * listInput[i][0]
                self.wTab[1] = self.wTab[1] + self.learningRate * (listeOutput[i] - predic) * listInput[i][1]
                self.wBiais = self.wBiais + self.learningRate * (listeOutput[i] - predic) * self.biais
                totalError += (1/2) * pow((predic - listeOutput[i]), 2)
            self.errorTab[k] = totalError
            self.converge()
        plt.plot(self.errorTab)
        plt.show()

"""if __name__ == '__main__':
    list = numpy.array([[0,0], [0,1], [1,0], [1,1]])
    listResult = numpy.array([0, 0, 0, 1])
    w1 = -5
    w2 = -5

    wTab = numpy.zeros([10,10])
    totalError = 0
    for i in range(10):
        for j in range(10):
            tempError = 0
            resultNeural = 0
            calc1 = w1 * list[0][0] + w2 * list[0][1]
            if(calc1 > 0):
                resultNeural = 1
            else:
                resultNeural = 0
            tempError = (1/2) * pow((resultNeural - listResult[0]),2)
            totalError = tempError
            calc2 = w1 * list[1][0] + w2 * list[1][1]
            if (calc2 > 0):
                resultNeural = 1
            else:
                resultNeural = 0
            tempError = (1/2) * pow((resultNeural - listResult[1]),2)
            totalError += tempError
            calc3 = w1 * list[2][0] + w2 * list[2][1]
            if (calc3 > 0):
                resultNeural = 1
            else:
                resultNeural = 0
            tempError = (1/2) * pow((resultNeural - listResult[2]),2)
            totalError += tempError
            calc4 = w1 * list[3][0] + w2 * list[3][1]
            if (calc4 > 0):
                resultNeural = 1
            else:
                resultNeural = 0
            tempError = (1/2) * pow((resultNeural - listResult[3]),2)
            totalError += tempError

            wTab[i][j] = totalError
            w2 += 1
        w2 = -5
        w1 += 1
    print(wTab)
    plt.imshow(wTab)
    plt.colorbar()
    plt.show() """