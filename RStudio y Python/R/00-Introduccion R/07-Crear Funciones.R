x = 4

doble = function(y){2*y}

doble(x)


funcionCuadrado = function(z){z^2}
funcionCuadrado(x)


#Funcion f(x)=x^3 - 3^x * sen(x)

fx = function(j){j^3 - 3^j * sin(j)}

fx(x)
fx(5)
fx(pi/2)

fy = function(j){
  j^3 - 3^j * sin(j)
  }

producto = function(x,y){
  x*y
}

producto(2,2)


suma1 = function(x){
  x+1
}

suma5 = function(numero){
  numero = suma1(numero);
  numero = suma1(numero);
  numero = suma1(numero);
  numero = suma1(numero);
  suma1(numero)
}

suma5(3)

ls() #Lista las variables y funciones creadas

rm(doble) #Remueve funcion o variable creada

#Es mejor usar la escobita
