import Perceptron
import numpy

if __name__ == '__main__':
    Percep = Perceptron.Perceptron(2, 10, 0.01, 'weight.csv')
    listInput = numpy.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    listResult = numpy.array([0, 0, 0, 1])
    Percep.train(listInput, listResult)
    res = Percep.predict(0, 0)
    res1 = Percep.predict(0, 1)
    res2 = Percep.predict(1, 0)
    res3 = Percep.predict(1, 1)
    print(res)
    print(res1)
    print(res2)
    print(res3)
