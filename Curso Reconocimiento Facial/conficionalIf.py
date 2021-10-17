#Ejercicio 1

valor1 = int(input("Ingrese el primer valor = "))
valor2 = int(input("Ingrese el segundo valor = "))

if (valor1%2 == 0 and valor2%2==0):
    print(f"El {valor1} y el {valor2} son pares")

elif (valor2%2==0 and valor1%2 != 0):
    print(f"El {valor2} es par")

elif (valor2%2!=0 and valor1%2 == 0):
    print(f"El {valor1} es par")

else:
    print(f"Ni el {valor1} y ni el {valor2} son pares")


#Ejercicio 2

valor1 = int(input("Ingrese el primer valor = "))
valor2 = int(input("Ingrese el segundo valor = "))
valor3 = int(input("Ingrese el primer valor = "))

if(valor1<valor2<valor3):
    print(f"El {valor3} es el numero mayor")

elif(valor3<valor2<valor1):
    print(f"El {valor1} es el numero mayor")

else:
    print(f"El {valor2} es el numero mayor")

#Ejercicio 3

print("Bienvenido al cajeto automaticos, elija una opcion")
print("1. Ingreso dinero")
print("2. Retirar dinero")
print("3. Mostrar dinero")
print("4. Salir")

saldo = 2000

opcion = int(input("Elija una opcion = "))

if (opcion == 1):
    print("Opcion Ingresar dinero")
    ingreso = int(input("¿Cuanto dinero va a Ingresar? = "))
    print("Dinero Ingresado = ", ingreso," Tu nuevo saldo es de = ", saldo+ingreso)
elif(opcion == 2):
    print("Opcion Retirar dinero")
    retiro = int(input("¿Cuanto dinero va a Retirar? = "))

    if(saldo-retiro >= 0):
        print("Dinero Retirado = ", retiro," Tu nuevo saldo es de = ", saldo-retiro)

    else:
        print("Lo siento la cantidad que quiere retirar supera los limites")
elif(opcion == 3):
    print("Opcion Mostrar dinero")
    print("Tu nuevo saldo es de = ", saldo)
else:
    print("Muchas Gracias por venir")