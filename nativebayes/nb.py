__author__ = 'kuangzhexi'

import numpy as np


class NativeBayes:
    def __init__(self):
        pass

    def fit(self, x, y):
        pass

    def predict(self, x):
        pass



if __name__ == "__main__":
    with open("./test_file", "rb") as fin:
        for line in fin:
            tokens = line.rstrip("\n").split(" ")
            lable = tokens[0]
            featurs = tokens[1:]