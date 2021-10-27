import numpy as np

L1 = [1,2,3,4,5,6,7,8] #Simplemente crear una lista
#Numpy puede crear en objeto apartir del array 
x1 = np.array(L1)
print(x1)

x2 = np.array(L1, dtype="float32")
print(x2)

#Tipos de datos
#bool_
#int_, intc , intp, int8, int16, int32, int64
#uint8 , uint16, uint32, uint64
# float_, float16, float32, float64
# complex_,complex64, complex128

matrix = np.zeros((3,4))
print(matrix)

matrix2 = np.ones((3,4))
print(matrix2)

matrix3 = np.arange(10)
print(matrix3)

matrix4 = np.arange(3,12, dtype=np.float32)
print(matrix4)

matrix5 = np.arange(3,12,0.5)
print(matrix5)

matrix6 = np.linspace(1.,7.,12)
print(matrix6)

matrix7 = np.eye(5)
print(matrix7)

matrix8 = np.zeros((8,3))
matrix8.reshape((6,4))
print(matrix8)

matrix9 = np.arange(24)
matrix9.reshape((6,4))
print(matrix9)

matrix10 = np.array([[1,2,3,4,5,6,7,8],[2,1,4,5,6,8,9,3]])
print(matrix10)
np.ravel(matrix10)
print(matrix10)

matrix10.flatten()
np.transpose(matrix10)
np.resize(matrix10,(5,3))






