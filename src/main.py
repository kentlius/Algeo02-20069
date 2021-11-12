import numpy as np
from PIL import Image
from U import *
from Eigen import *
from VTranspose import *


def openImage(imagePath):
    imOrig = Image.open(imagePath)
    im = np.array(imOrig)

    R = im[:, :, 0]
    G = im[:, :, 1]
    B = im[:, :, 2]

    return [R, G, B]


def compressSingleChannel(color, k):
    # ganti untuk sesuaiin
    # UChannel, SigmaChannel, VHChannel = np.linalg.svd(color)
    UChannel, X, VHChannel = np.linalg.svd(color)
    # UChannel = U(color)
    SigmaChannel = EigenValue(color @ color.T)
    # VHChannel = VTranspose(color)
    #np.diag(SigmaChannel)[0:k, 0:k]
    # SigmaChannel[0:k]
    Compressed = np.zeros((color.shape[0], color.shape[1]))
    # ImgCompressed = (
    #     UChannel[:, 0:k] @ SigmaChannel[0:k] @ VHChannel[0:k, :])

    ImgCompressed = (
        UChannel[:, 0:k] @ np.diag(SigmaChannel)[0:k, 0:k] @ VHChannel[0:k, :])
    Compressed = ImgCompressed.astype('uint8')
    return Compressed


# ubah foto dari website
R, G, B = openImage('test/lena.png')
# # im = Image.open('test/lena.png')
# # width, height = im.size
# # print(width, height)

# # menerima berapa persen kompressi
SVL = round(10.5)

RC = compressSingleChannel(R, SVL)
GC = compressSingleChannel(G, SVL)
BC = compressSingleChannel(B, SVL)

newR = Image.fromarray(RC, mode=None)
newG = Image.fromarray(GC, mode=None)
newB = Image.fromarray(BC, mode=None)

newImage = Image.merge("RGB", (newR, newG, newB))

# OImage.show()
newImage.show()

# X, S, Y = np.linalg.svd(R)
# print(EigenValue(R @ R.T))
# print(S)
