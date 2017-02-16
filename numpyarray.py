import zipfile

from numpy import *
from numpy.core.defchararray import array
from numpy.core.multiarray import arange
import os
a = arange(9)
a.shape = (3,3,1)

CannedImages = zipfile.ZipFile("C:\\archive\\gerrit\\BurtonInstrument\\src\\focus_images\\focus_images.zip")
inputImage = CannedImages.open("image0500.png").read()


a = bytearray(memoryview(inputImage))
b = a[0:6]

if 'PNG' in b:
    print "success"
else:
    print "failure"
