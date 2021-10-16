import math

print("Hola Mundo")

calculo = (5+(9/3))**2

print(calculo)

#Ejercicio

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

calculo = ((c+5)*(b**2-3*a*c)*a**2)/(4*a)

print("El resultado es = ",calculo)

#Ejercicio 2

a = 20
b = 30

a,b = b,a

print("El valor de a es = ",a)
print("El valor de b es = ",b)


#Ejercicio 3

r = float(input("Ingrese el radio del circulo = ")) 

area = math.pi*(r**2)

longitud = 2*math.pi*r

print(f"El area del circulo es {area:.1f}")
print(f"La longitud del circulo es {longitud:.1f}")


#Ejercicio 4

compra = float(input("Ingrese el valor de la compra = "))

descuento = compra*(36/100)

precioFinal = compra-descuento

print(f"El precio final con el descuento del 36% es de {precioFinal}")
 