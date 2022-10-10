import os
import numpy as np

from sklearn import preprocessing
from sklearn.preprocessing import minmax_scale

def readData(filename, folder = ""):
    dt = np.loadtxt(os.path.join(folder, filename), delimiter=",")
    X, y = dt[:, 0:2], dt[:, 2]
    X = np.column_stack((np.ones(y.shape[0]), X))
    return X, y.reshape(y.shape[0],1)

def calculateLoss(X, y, w):
    h = np.dot(X, w)
    m = y.shape[0]
    J = (1/(2*m))*np.sum(np.square(h - y))
    return J

def gradientDescent(X, y, alpha = 0.01, n = 1500):
    w = np.zeros((X.shape[1],1))
    temp = []
    m = y.shape[0]
    for i in range(n):
        w = w - (alpha/m)*np.dot(X.T, (np.dot(X, w)-y))
        temp.append(calculateLoss(X, y, w))
    return w, temp

def main():
    X, y = readData("ex1data2.txt")
    X[:,1:] = minmax_scale(X[:,1:], axis = 0)
    y = minmax_scale(y, axis = 0)
    print(X, y)
    w, ll = gradientDescent(X, y)
    print("Giá trị vector trọng số tối ưu tìm được theo thuật toán Gradient Descent - w_optimal:", w.T)

if __name__ == '__main__':
    main()

