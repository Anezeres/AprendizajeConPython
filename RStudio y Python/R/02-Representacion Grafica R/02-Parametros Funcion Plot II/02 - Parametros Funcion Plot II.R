#type = tipo de grafico que queremos 
#
#p , producirá un grafico de puntos
#l , producirá un grafico de lineas rectas, las lineas no transpasan los puntos
#b , producirá un grafico de linea que une los puntos
#o , producirá un grafico de linea que une los puntos, que si transpasan los puntos
#h , producirá un histrograma
#s , producirá un histrograma de escalones
#n ,  no producirá puntos

#como se ve en la imagen adjunta en la carpeta, siempre se pone al final el parametro 
#par(mfrow = c(1,1))


#para los graficos de lineas

#lty, sirve para especificar el tipo de linea

#con 4 tipos diferentes :
#"solid" : 1,  linea continua
#"dashed" : 2,  linea discontinua
#"dotted" : 3,  linea de puntos
#"dotdashed" : 4,  linea que alterna puntos y rayas
 
#lwd, sirve para cambiar el grosor de la linea
#xlim, sirve para modificar el rango de x
#ylim, sirve para modificar el rango de y
#xaxp, sirve para modificar posiciones de las marcas de x
#yaxp, sirve para modificar posiciones de las marcas de y



#xaxp = c(0,40,2) Quiero de 0 a 40, con solo 2 divisiones 
#yaxp = c(-100,100,8) Quiero de -100 a 100, con solo 8 divisiones 

#para ayuda ?plot, ?par





