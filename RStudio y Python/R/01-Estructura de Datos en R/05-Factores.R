#Factores levels
#Primero se crea un vector y luego se transforma por medio de factor()
#O por medio de as.factor()

nombres = c("Julian", "Juan","Maria", "Carlos","Antonio","Maria")

nombres.factor = factor(nombres)
nombres.factor

#Factor es como una etiqueta, pais de procedencia, el genero, forma de clasificacion

#Funcion factor(vector, levels=)
#labels, permite cambiar los nombres de los niveles
levels(factor) #obtener los niveles del factor

genero = c("H","M","M","H","M","H","M","M")
genero.factor = factor(genero)
genero.factor


genero.factor3 = factor(genero,levels = c("M","H","B"))
genero.factor3

genero.factor4 = factor(genero,levels = c("M","H","B"),labels = c("Mujer","Hombre","Bi sexo"))
genero.factor4


#Con labels se pueden gestionar muy bien los datos