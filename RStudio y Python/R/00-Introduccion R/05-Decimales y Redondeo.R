sqrt(2)

#Pero ahora quiero 10 digitos

print(sqrt(2),10)

#Redondear

round(sqrt(2),3)

#floor  redondeo a la baja

floor(sqrt(2)) 

#ceiling redondeo a la alza

ceiling(sqrt(2))

#trunc no hay diferencia con el floor

trunc(sqrt(2))


#Cuando hacemos operaciones gordas por comas flotantes

sqrt(2)^2 #Magnifico
sqrt(2)^2-2 #No es 0, si no 4.440892e-16, no es 0, pero casi

#Se acumulan errores de redondeo y de manipulacion algebraica

2^50 #notacion cienfitica
print(2^50,15) #Notacion exacta
print(2^50,2) #2 cifras significativas

print(pi,22) #ir con cuidado a la hora de pedir mas de 16 digitos pq R se empieza
#a equivocar

#Round reondea a la cifra par

round(1.35,1)

#Round a 0, R entiende que lo quieres redondiar al entero mas cercano

round(sqrt(2),0)
round(sqrt(2)) #Tambien si no le dices nada, round entiende que el parametro es 0
