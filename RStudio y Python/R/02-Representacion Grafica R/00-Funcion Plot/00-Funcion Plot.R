#Funcion plot

plot(x,y)
plot(x) = plot(1:length(x),x)

plot(x,funcion) #Para dibujar el grafico de la funcion


alumnos = c(1:10)
notas = c(2,5,6,4,7,8,9,5,2,1)
plot(alumnos,notas) #plot(x,y)

```{r primer_plot, fig.cap="Grafico basico explicando el uso de plot"} #Se puede poner etiquedas dentro de {r}
x = c(1,2,3,-4,5,6,7,-8,9,10)
y = c(7,8,9,6,2,1,4,5,6,3)
plot(x,y)

#fig.align='center' para alinear en el centro
#fig.cap="Grafico basico explicando el uso de plot" para poner un pie del grafico
#Hay muchos fig. parametro para poner bonito el HTML
#Se utilizan $$ para escribir funciones