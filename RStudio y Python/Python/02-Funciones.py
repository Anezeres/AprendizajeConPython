def suma(x,y): #Esta es una funcion
    print(x+y) 


class Operaciones(object):

    def suma(self,x,y):
        self.resultado = x+y #A la propia clase le asigno un resultado, este es un metodo
        print(self.resultado)



suma(3,1)

#Primero se crea una instancia o un objeto de la clase
Instancia = Operaciones()
Instancia.suma(3,1) #Esta sintaxis es un poco mas compleja, hay que crear primero un objeto de la clase y luego invocar al metodo