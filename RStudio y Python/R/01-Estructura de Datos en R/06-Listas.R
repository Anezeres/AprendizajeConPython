#Vectores tenian una restriccion tenian que ser de un solo tipo
# list()

#list[[i]]

x = c(1:25)
L = list(nombre = "Temperaturas",datos = x, media = mean(x), sumas= cumsum(x)) 
L

#Uno entra como argumento las propias variables de la lista

#Para obtener una determinada componente de una lista
L$nombre
L$datos
L[[3]]
L[[2]]
L[[1]]

3*L[[2]]

#obtener la informacion de una lista str() names(list)

names(L)
str(L)
