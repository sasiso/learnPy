from numpy import *
from numpy.core.multiarray import arange

a = arange(15).reshape(3, 5)
print a.shape
print a.ndim
print a.itemsize
print a.size


print type(zeros((3, 4)))
