import math


print(math.exp(3)) #Esta funcion es mucho mas precisa 
print(math.e**3) #Que invocar la variable e y exponer


print(math.pow(math.e,3)) #Que invocar la variable e y exponer



print(math.log(12)) #Si no le especificas toma logaritmo base e 
print(math.log(12,2)) 


print(math.log2(32)) 
print(math.log10(100)) 


print(math.sqrt(100)) 

print(math.sin(180)) #El argumento tiene que estar en radianes, no son 180 grados, si no, 180 Radianes
print(math.cos(math.pi))
print(math.tan(math.pi/2))
print(math.asin(1))
print(math.acos(0))
print(math.atan(1)) #= 0.7853981633974483

#Ahora, hay una funciona math.degrees que convierte de ranidanes a grados

print(math.degrees(0.7853981633974483)) #= 0.7853981633974483 = 45°
print(math.radians(60)) #=  60° = 1.0471975511965976 Radianes
print(math.cos(math.radians(60))) #=  60° = 1.0471975511965976 Radianes

#Longitud de un vector

print(math.hypot(3,4)) #Hipotenusa
print(math.atan2(4,3)) #El angulo que forma con el eje x, está girado (y,x) resultado en radianes
print(math.degrees(math.atan2(4,3))) #El angulo que forma con el eje x, está girado (y,x) resultado en radianes

#Funciones hiperbolicas

print(math.sinh(0)) #
print(math.cosh(0)) #
print(math.tanh(0)) #

#unas que no entendí muy bien, pero tienen que ver con estadistica y campanas de gauss

print(math.erf(math.pi)) # 
print(math.erfc(math.pi)) # Lo que le falta a la funcion anterior para llegar a 1
print(math.erfc(math.pi)+math.erf(math.pi)) # Lo que le falta a la funcion anterior para llegar a 1


print(math.gamma(2)) # Factorial de n-1
print(math.lgamma(2)) # Factorial de n-1







