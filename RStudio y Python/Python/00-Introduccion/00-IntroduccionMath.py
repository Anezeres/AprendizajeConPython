import math

print(math.pi)
print(math.e)
print(math.tau)
print(math.inf)
print(-math.inf)
print(math.nan)
#print(math.sqrt(-1))
#print(math.log(0))
#print(math.exp(10000)) Python no está preparada para esta memoria

#La libreria no está pensada para utilizar el nan

math.pow(math.nan,0)

#Representacion Numerica

print(math.ceil(3.4561)) #Redondeo a la alza
print(math.floor(3.4561)) #Redondeo a la Baja
print(math.trunc(3.4561)) #Coloca el numero natural mas cercano, quita decimales



print(math.copysign(3.4561,-1)) #Copia el signo
print(math.fabs(-5)) #Por el numero Absoluto


print(2**5) #Potencia
print(math.factorial(5)) #Devuelve el numero de la funcion factorial

#Creo que no existe libreria de numero combinatorio como en R

x = 5
y = 2

print(math.factorial(x)/(math.factorial(y)*math.factorial(x-y)))


#Problema con el modulo

print(math.fmod(7,3)) #Este es mas exacto en cuanto a numeros reales se refieres
print(7%3) #No lo recomiendan mucho puesto que solo se trata del modulo entre enteros


print(2/5) #Divicion decimal
print(2//5) #Division Entera

#Este está muy interesante

print(math.modf(4.23565)) #Este Separa la parte entera de la parte decimal
print(math.gcd(12,36,24)) #Maximo como un divisor

#Este tambien está interesante para el uso de condicionales
print(math.isfinite(2.26)) #Maximo como un divisor True
print(math.isinf(2.26)) #Maximo como un divisor False









