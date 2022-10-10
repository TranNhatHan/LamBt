import os
import numpy as np

from sklearn.preprocessing import minmax_scale
#
# def readData(filename, folder = ""):
#     dt = np.loadtxt(os.path.join(folder, filename), delimiter=",")
#     X, y = dt[:, 0:2], dt[:, 2]
#     X = np.column_stack((np.ones(y.shape[0]), X))
#     return X, y.reshape(y.shape[0],1)
#
# def calculateLoss(X, y, w):
#     h = np.dot(X, w)
#     m = y.shape[0]
#     J = (1/(2*m))*np.sum(np.square(h - y))
#     return J
#
# def gradientDescent(X, y, alpha = 0.01, n = 1500):
#     w = np.zeros((X.shape[1],1))
#     temp = []
#     m = y.shape[0]
#     for i in range(n):
#         w = w - (alpha/m)*np.dot(X.T, (np.dot(X, w)-y))
#         temp.append(calculateLoss(X, y, w))
#     return w, temp
#
# def main():
#     X, y = readData("ex1data2.txt")
#     X[:,1:] = minmax_scale(X[:,1:], axis = 0)
#     y = minmax_scale(y, axis = 0)
#     w, ll = gradientDescent(X, y)
#     print("Giá trị vector trọng số tối ưu tìm được theo thuật toán Gradient Descent - w_optimal:", w.T)
#
# if __name__ == '__main__':
#     main()

class LogisticRegression:

    def __init__(self, X, y, alpha=0.01, n=2000):
        self.X = X
        self.y = y
        self.alpha = alpha
        self.n = n
        self.w = np.zeros((X.shape[1], 1))

    def calculate_loss(self):
        h = 1/(1+np.exp(-np.dot(self.X, self.w)))
        m = self.y.shape[0]
        J = (-1/m) * (np.dot(self.y.T, np.log(h)) + np.dot((1-self.y).T, np.log(1-h)))
        return J

    def gradient_descent(self):
        w = np.zeros((self.X.shape[1], 1))
        temp = []
        m = self.y.shape[0]
        for i in range(self.n):
            if i == 0:
                w = w - (self.alpha/m) * np.dot(self.X.T, 1/(1+np.exp(-np.dot(self.X, self.w))) - self.y)
        self.w = w

    def predict(self, x):
        h_w = 1 / (1 + np.exp(- np.dot(x, self.w)))
        print(h_w)
        if h_w[0, 0] >= 0.5:
            return 1
        else:
            return 0

def read_data(filename, folder = ""):
    dt = np.loadtxt(os.path.join(folder, filename), delimiter=",")
    X, y = dt[:, :-1], dt[:, -1]
    X = np.column_stack((np.ones(y.shape[0]), X))
    return X, y.reshape(y.shape[0], 1)

def main():
    X, y = read_data("ex2data1.txt")
    # X[:,1:] = minmax_scale(X[:,1:], axis = 0)
    # y = minmax_scale(y, axis = 0)
    lr = LogisticRegression(X, y)
    lr.gradient_descent()

if __name__ == '__main__':
    main()