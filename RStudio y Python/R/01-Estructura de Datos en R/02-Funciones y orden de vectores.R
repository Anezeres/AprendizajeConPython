x = 1:10
x

x + pi
x - pi
x * pi
x / pi

2^x
x^2


sapply(x, FUN = function(elemento){sqrt(elemento)})

cd = function(x){summary(lm((1:4)~c(1:3,x)))$r.squared}
cd(5)
cd(x) #Error

#Y para eso se usa el sappy

sapply(x,FUN=cd)


#Se pueden sumar vectores muy facilmente

1:10 + 1:10
(1:10)*(1:10)
(1:10)^(1:10)

n = 1:100
x = 2*3^(n/2)-15
x


y = n^2/(n^2+1)
y



length(1:100)


#Funciones

cuadrado = function(x){x^2}

v = c(1:6)

sapply(v, FUN=cuadrado)
mean(v)
cumsum(v)

v = c(1,5,4,7,8,9,3,1)
rev(v)
sort(v)


vectorDecreciente = function(v){
  rev(sort(v))
}

vectorDecreciente(v)

#?sort


