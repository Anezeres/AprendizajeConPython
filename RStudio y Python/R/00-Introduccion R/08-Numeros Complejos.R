z = 2+3i


z2 = complex(real = 2,imaginary = -3)

Re(z) # = 2

Im(z) # = 3

Conj(z2)

#Operaciones con numeros complejos

numeroC = 3+2i
numeroC2 = -1+3i

class(numeroC)

numeroC*5

numeroC * numeroC2
numeroC / numeroC2


#No es necesario poner el asterisco 2+3*i

pi + sqrt(2)i

#Si es racional o entero es mejor usar la funcion complex

complex(real = pi, imaginary=sqrt(2))

#No se puede sacar raiz cuadrada de negativos

sqrt(-2)

sqrt(as.complex(-2))


#La raiz cuadrada siempre devuelve la parte positiva
sqrt(numeroC)
exp(numeroC)
sin(numeroC)
cos(numeroC)

#Modulo = sqrt(Re(z)^2 + Im(z)^2)

Mod(numeroC2)

#Argumento = arctan(Im(z)/Re(z))
Arg(numeroC)

#Conjugado = Re(z) - Im(z)i

Conj(numeroC)
