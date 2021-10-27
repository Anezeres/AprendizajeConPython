v = c(1:10)

v[5]

v[-c(5,8)] #Escribe un subvector, pero quita los elementos dados en el c()

#Y creando un filtro

v[v>3 & v<7]


x = seq(3,50,by=3.5)
x

x[3]
x[8]
x[length(x)]
x[length(x)-1]
x[length(x)-2]
x[-8]
x[-c(5,8,7,2,6)]
x[4:8]
x[8:4]
x[seq(2,length(x),by=2)]
x[seq(1,length(x),by=2)]
x[-seq(2,length(x),by=2)]
x[(length(x)-3):length(x)]
x[x<20]
x>30 #ME genera un vecto de booleanos
x[x>30]#ME genera aquellos que cumplen esa condicion

#Se pueden hacer comparanciones con otros vectores

y = c(1,5,8,9,6,3,1,4,8,9)
x = c(-2,1,-8,4,-6,3,-1,8,-8,9)
x>0 #Array de booleanos
y[x>0] #Acá va a imprimir solo aquellas posiciones que cumplan con la condicion

which(x>4) #Which me entrega las posiciones, muy importante, no los datos
which(y>4)

#Para acceder a esos numeros debo hacer
which(x>4) #Which me entrega las posiciones, muy importante, no los datos
x[which(x>4)] #Notece la diferencia, este me entrega los datos, no las posiciones

which.min(x)
x[which.min(x)]


x = c()
x
y = NULL

z = c(7,5,x,4,y) #Los valores nulos, nunca salen en pantalla
z
