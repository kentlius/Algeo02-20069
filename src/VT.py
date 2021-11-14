from Eigen import *

def VTranspose(A):
    ATA = A.T @ A #Perkalian matriks A transpose dengan matriks A
    nilai, vektor = find_eig_qr(ATA) #Mendapat nilai eigen dan vektor eigen

    VT = vektor.T #Transpose V

    return VT