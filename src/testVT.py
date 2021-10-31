import numpy
from PIL import Image
from VTranspose import *

# open the image and return 3 matrices, each corresponding to one channel (R, G and B channels)
def openImage(imagePath):
    imOrig = Image.open(imagePath)
    im = numpy.array(imOrig)

    aRed = im[:, :, 0]
    aGreen = im[:, :, 1]
    aBlue = im[:, :, 2]

    return [aRed, aGreen, aBlue]

aRed, aGreen, aBlue = openImage('test/lena.png')

VT_aRed = VTranspose(aRed)

print(VT_aRed)