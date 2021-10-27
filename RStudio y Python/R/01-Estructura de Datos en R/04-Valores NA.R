2^pi > pi^2 #Falso
2^pi
pi^2 

#Sirven para tener respuestas booleanas

x = 1:10

x[11]
x[11] = 20
x

x[2:5] = x[2:6] + 3
x
x[5:4] = 0
x

x = 1:10
x
x[length(x)+5] = 20 #1  2  3  4  5  6  7  8  9 10 NA NA NA NA 20
x


#NA Not Avaliable, y con los NA, dan dolor de cabeza, pq no se puede operar
#Con ellos

sum(x)
sum(x, na.rm = TRUE)
mean(x,na.rm = TRUE)

#El NA no es un valor, si no un concepto
is.na(x) #Devuelve un array de booleanos, ahora si se puede usar el which

which(is.na(x))
x[which(is.na(x))]


#En estadisticas al parecer, se suele reemplazar los valores NA por la media

y = x

y[is.na(y)] = mean(y, na.rm=TRUE)
y
na.omit(y)

cumsum(na.omit(x))
