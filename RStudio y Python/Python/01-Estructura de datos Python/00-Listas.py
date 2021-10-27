L5 = [0]*10
print(L5)

L5[2] = 20
print(L5)

print(L5[1:4])

L5.append(30)
print(L5)


L5.remove(30) #Elimina la primera ocurrencia del objeto
print(L5) 

L6 = [1,2,3,4,5,6]
print(L6[1::2])
print(L6[::2])