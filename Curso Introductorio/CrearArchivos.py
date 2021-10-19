def crearArchivo():
    archivo = open("datos.txt","w")
    archivo.close()

def escribirArchivo():
    archivo = open("datos.txt","a")
    archivo.write("Julian Alvarez")
    archivo.write("310")
    archivo.close()

def leerArchivo():
    archivo = open("datos.txt","r")
    linea = archivo.readline()

    while linea != "":
        print(linea)
        linea = archivo.readline()
    
    archivo.close()

crearArchivo()
escribirArchivo()