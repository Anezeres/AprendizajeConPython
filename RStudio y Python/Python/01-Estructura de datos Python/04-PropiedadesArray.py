import numpy as np
from numpy.core.fromnumeric import reshape

x = np.arange(12)
x = reshape(x,(3,4))
print(x)

print(x.ndim)
print(x.shape)
print(x.size)
print(x.dtype)
print(x.itemsize)
print(x.data)
print(x[2])
print(x[2,1])
x.shape = (4,3)
print(x)
print(x[0:2, 2:4])


x = np.arange(50)
print(x)
print(x[x>30])
condicion = x<25
print(condicion)
print(x[condicion])


x[12:24] = 1
print(x)







