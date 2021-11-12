import numpy as np
from numpy import linalg

def U(A):
    Uz, S, VT = linalg.svd(A) #ambil S dan VT dari A

    Sigmainv = np.zeros(A.shape) #matrix nol dengan bentuk A
    np.fill_diagonal(Sigmainv, np.reciprocal(S)) #isi matriks dengan sigma reciprocal

    VTinv = linalg.inv(VT) #inverse VT

    Uinv = A @ VTinv @ Sigmainv.T
    # U = linalg.inv(Uinv)

    return Uinv


# A = np.array([  [1, 2, -1],
#                 [2, 1, -1],   ]) #Contoh matriks A

# print(U(A))