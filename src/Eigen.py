import numpy as np


def find_eig_qr(A):
    Sigma = []
    pQ = np.eye(A.shape[0])
    X = A.copy()
    for i in range(100):
        Q, R = np.linalg.qr(X)
        pQ = pQ @ Q
        X = R @ Q
    return np.diag(X), pQ
    # np.diag(X) adalah eigen value, pQ adalah eigen vector


def Sigma(A):
    S = []
    M, _ = find_eig_qr(A @ A.T)
    for i in range(len(M)):
        S.append(np.abs(M[i]))
    return S