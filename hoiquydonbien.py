import os
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import Ridge


def readData(filename, folder = ""):
    dt = np.loadtxt(os.path.join(folder, filename), delimiter=",")
    X, y = dt[:, 0], dt[:, 1]
    X = np.stack([np.ones(y.shape[0]), X], axis=1)
    return X, y

def calculateLoss(X, y, w):
    h = np.dot(X, w)
    m = y.shape[0]
    J = (1/(2*m))*np.sum(np.square(h - y))
    return J

def gradientDescent(X, y, w = [0, 0], alpha = 0.01, n = 1500):
    temp = []
    m = y.shape[0]
    for i in range(n):
        w = w - (alpha/m)*(np.dot(X, w) - y).dot(X)
        temp.append(calculateLoss(X, y, w))
    return w, temp

def main():
    X, y = readData("ex1data1.txt")
    w, ll = gradientDescent(X, y)
    print("Giá trị vector trọng số tối ưu tìm được theo thuật toán Gradient Descent - w_optimal:", w)
    print("List chứa tất cả các giá trị của hàm mất mát tương ứng với các giá trị vector trọng số tại mỗi bước lặp:", ll)

def mainsklearn():
    dt = np.loadtxt("ex1data1.txt", delimiter=",")
    X, y = dt[:, 0], dt[:, 1]
    reg = LinearRegression()
    reg.fit(X.reshape(-1, 1), y)
    print(reg.coef_[0], reg.intercept_)

if __name__ == "__main__":
    mainsklearn()
    # [-3.63029144  1.16636235]