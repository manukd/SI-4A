import csv
import Perceptron
import numpy

import Perceptron_10output


def read(filenameCSV, rows, cols):
    Tab = numpy.zeros((rows, cols), dtype=int)
    with (open(filenameCSV)) as csvfile:
        line_count = 0
        read = csv.reader(csvfile, delimiter=';')
        for row in read:
            if line_count < rows:
                for i in range(cols):
                    Tab[line_count][i] = float(row[i])
                line_count += 1
    return Tab

def convertB(tab):
        res = 0
        for i in range(len(tab)):
            if tab[i] > 0:
                res += pow(2, i)
        return res

if __name__ == '__main__':
    Percep = Perceptron.Perceptron(2, 300, 0.01, 'weight.csv')
    Percep10 = Perceptron_10output.Perceptron(2, 300, 0.01, 'weight.csv')
    listInput = read('input.csv', 10, 7)
    listResult = read('output.csv', 10, 4)
    listResult10 = read('output_10output.csv', 10, 10)
    """Percep.train(listInput, listResult)"""
    Percep10.train(listInput, listResult10)
    tab = numpy.zeros((10,1))
    """for i in range(10):
        for j in range(4):
            res = Percep.predict(listInput[i], j)
            tab[3 - j] = round(res)
        decimal = convertB(tab)
        print(decimal)"""
    for i in range(10):
        for j in range(10):
            res = Percep10.predict(listInput[i], j)
            tab[9 - j] = round(res)
        decimal = convertB(tab)
        print(decimal)
