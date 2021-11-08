import numpy as np

def U(A):
    AAT = A @ np.transpose(A) #Perkalian matriks A transpose dengan matriks A
    nilai, vektor = np.linalg.eig(AAT) #Mendapat nilai eigen dan vektor eigen

    for i in range(2):
        vektor[:,i] /= np.linalg.norm(vektor[:,i]) #Normalisasi vektor eigen

    return vektor


# A = np.array([  [3, 1, 1],
#                 [-1, 3, 1]   ]) #Contoh matriks A

# U = U(A)

# print(U)