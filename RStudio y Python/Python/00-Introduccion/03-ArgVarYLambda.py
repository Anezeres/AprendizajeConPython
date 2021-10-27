#Cuando no sabemos el numero extacto de argumentos que queremos pasar, combiene una la sintaxis de asterisco

def suma(*args):
    print(sum(args))


suma(1,2,3,4,5,6)

def sumaCuadrados(*datos):
    total = 0

    for d in datos:
        total = total + d**2
    
    print(total)


sumaCuadrados(1,2)

#Funciones Anonimas

doble = lambda x: x*2

print(doble(4))

cuadrado = lambda x: x**2

print(cuadrado(4))

suma = lambda x,y: x+y

print(suma(4,3))


#from functools import reduce
from functools import reduce

numeros = [1,2,3,4,5,6,7,8,9,10]

numerosFiltrados = list(filter(lambda x: (x*2>8),numeros))

print(numerosFiltrados)

numerosMapeados = list(map(lambda x:(x*2),numeros))

print(numerosMapeados)


reducir = reduce(lambda x,y: x+y,numeros)



