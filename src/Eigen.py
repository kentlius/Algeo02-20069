import numpy as np


def EigenVector(M):
    X, Y = np.linalg.eig(M)
    return Y


def EigenValue(M):
    Out = []
    for i in range(10):
        Q, R = np.linalg.qr(M)
        M = R @ Q
    for i in range(len(M)):
        if (M[i][i] < 0):
            Out.append((M[i][i]*(-1))**(1/2))
        else:
            Out.append((M[i][i])**(1/2))
    Out.sort(reverse=True)
    return(Out)
