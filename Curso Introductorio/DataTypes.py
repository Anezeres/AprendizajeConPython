numero1 = 200.00230001
numero2 = 123.00101

resultado = numero1 - numero2

print(resultado)

print(round(resultado,3))



#----

comparacion1 = 2<33

comparacion2 = 33<2

print(comparacion1)
print(comparacion2)

#----

miTupla = (2,3,4,5,6)

print(type(miTupla))

#----

estudiantes = {"Sara":23,"Julian":23,"Jose":34}

print(type(estudiantes))

for x in estudiantes.values():
    print(x)

for y in estudiantes.keys():
    print(y)

for z in estudiantes.items():
    print(z)