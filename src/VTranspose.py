import numpy as np

def VTranspose(A):
    ATA = np.transpose(A) @ A #Perkalian matriks A transpose dengan matriks A
    nilai, vektor = np.linalg.eig(ATA) #Mendapat nilai eigen dan vektor eigen

    for i in range(3):
        vektor[:,i] /= np.linalg.norm(vektor[:,i]) #Normalisasi vektor eigen

    VT = np.transpose(vektor) #Transpose V(hasil normalisasi)

    return VT


# A = np.array([  [3, 1, 1],
#                 [-1, 3, 1]   ]) #Contoh matriks A

# VT = VTranspose(A)

# print(VT)