from genericpath import exists
import cv2
import os
import imutils as imutils

ruta = r"D:\Mis Documentos\Desktop\Python\Curso Python 1\Curso Reconocimiento Facial\Reconocimiento\Facial\haarcascade_frontalface_default.xml"

ruido = cv2.CascadeClassifier(ruta)


modelo = "FotosJulian"

ruta1 = r"D:/Mis Documentos\Desktop/Python/Curso Python 1/urso Reconocimiento Facial/Reconocimiento/Facial"
rutaCompleta = ruta1 + "/" + modelo


if (not os.path.exists(rutaCompleta)):
    os.makedirs(rutaCompleta)

camara = cv2.VideoCapture(0)

id = 0

while True:
    respuesta,captura = camara.read()

    if (respuesta==False):
        break

    captura = imutils.resize(captura,width =640)

    grises = cv2.cvtColor(captura, cv2.COLOR_BGR2GRAY)
    idCaptura = captura.copy()
    caras = ruido.detectMultiScale(grises,1.3,3)

    for (x,y,e1,e2) in caras:
        cv2.rectangle(captura,(x,y),(x+e1,y+e2),(0,225,0),2)
        rostroCapturado =idCaptura[y:y+e2,x+e1]
        rostroCapturado = cv2.resize(rostroCapturado,(160,160), interpolation= cv2.INTER_CUBIC)
        cv2.imwrite(rutaCompleta+"/imagen_{}.jpg".format(id), rostroCapturado)
        id+=1

    cv2.imshow("Resultado Rostro",captura)

    if id == 351 :
        break

camara.release()
cv2.destroyAllWindows()
