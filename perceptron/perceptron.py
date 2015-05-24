__author__ = 'kuangzhexi'


import random
import numpy as np


class Perceptron:
    def __init__(self):
        self.__w = np.zeros(0)
        self.__bias = 0
        self.__step = 1

    def judge(self, x, y):
        """

        :rtype : bool
        """
        num = self.__bias
        num += sum(self.__w * np.array(x))
        if num * y <= 0:
            return False
        return True

    def judge_all(self, x, y):
        """

        :rtype : bool
        """
        for ind in range(0, len(x)):
            if not self.judge(x[ind], y[ind]):
                return False
        return True

    def revision(self, x, y):
        """

        :rtype : null
        """
        self.__w += self.__step * y * np.array(x)
        self.__bias += self.__step * y

    def fit(self, x, y):
        self.__w = np.zeros(len(x[0]))
        while not self.judge_all(x, y):
            index = random.randint(0, len(x)-1)
            if not self.judge(x[index], y[index]):
                self.revision(x[index], y[index])

    def debug(self):
        print self.__w
        print self.__bias

if __name__ == "__main__":
    perceptron = Perceptron()
    with open('./test_file', 'r') as fin:
        features = []
        labels = []
        for line in fin:
            tokens = line.rstrip("\n").split(" ")
            labels.append(int(tokens[0]))
            features.append([int(i) for i in tokens[1:]])
        perceptron.fit(features, labels)
        print perceptron.debug()