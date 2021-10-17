from posix import listdir
import cv2 
import os 
import numpy
from time import time

dataRuta = r"D:/Mis Documentos\Desktop/Python/Curso Python 1/urso Reconocimiento Facial/Reconocimiento/Facial/Data"

listaData = os.listdir(dataRuta)
print("Dara",listaData)

ids = []
rostrosData = []
id = 0

tiempoInicial = time()

for fila in listaData:
    rutaCompleta = dataRuta+"/"+fila

    for archivo in os.listdir(rutaCompleta):


        print("Imagenes : ", fila + "/" + archivo)

        ids.apepend(id)
        rostrosData.append(cv2.imread(rutaCompleta+"/"+archivo, 0))
        #imagenes = cv2.imread(rutaCompleta+"/"+archivo,0)
    
    tiempoFinalLectura = time()
    tiempoTotalLectura = tiempoFinalLectura-tiempoInicial

    print("Tiempo Total: ", tiempoTotalLectura)

    id = id+1

entrenamientoModelo1 = cv2.face.EigenRecognizer_create()

entrenamientoModelo1.train(rostrosData.numpy.array(ids))

tiempoFinalEntrenamiento = time()
tiempoTotalEntrenamiento = tiempoFinalEntrenamiento - tiempoTotalLectura

print("Tiempo de entrenamiento = ", tiempoTotalEntrenamiento)


entrenamientoModelo1.write("Entrenamiento Modelo1.xml")

print("Entrenamiento Cumplido")



