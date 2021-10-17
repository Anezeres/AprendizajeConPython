import cv2 
import os

dataRuta = r"D:/Mis Documentos\Desktop/Python/Curso Python 1/urso Reconocimiento Facial/Reconocimiento/Facial/Data"

listaData = os.listdir(dataRuta)
print("Dara",listaData)

entrenamientoModelo1 = cv2.face.EigenRecognizer_create()


entrenamientoModelo1.read("Entrenamiento Modelo1.xml")

ruidos = cv2.CascadeClassifier("D:\Mis Documentos\Desktop\Python\Curso Python 1\Curso Reconocimiento Facial\Reconocimiento\Facial\haarcascade_frontalface_default.xml")

camara = cv2.VideoCapture(0)

while True:
    _,captura = camara.read()
    grises = cv2.cvtColor(captura,cv2.COLOR_BGR2GRAY)

    idCaptura = grises.copy()
    cara = ruidos.detectMultiScale(grises, 1.3,5)

    for (x,y,e1,e2) in cara:
        #cv2.rectangle(captura,(x,y),(x+e1,y+e2),(0,225,0),2)
        rostroCapturado =idCaptura[y:y+e2,x+e1]
        rostroCapturado = cv2.resize(rostroCapturado,(160,160), interpolation= cv2.INTER_CUBIC)
        resultado = entrenamientoModelo1.predict(rostroCapturado) 
        cv2.putText(captura,"{}".format(resultado),(x,y-5),1,1.3,(0,255,0),1,cv2.LINE_AA)

        if resultado[1]<9000:
            cv2.putText(captura,"No encontrado",(x,y-20),2,1.1,(0,255,0),1,cv2.LINE_AA)

        else:
            cv2.putText(captura,"{}".format(resultado[0]),(x,y-20),2,0.7,(0,255,0),1,cv2.LINE_AA)



        cv2.rectangle(captura,(x,y),(x+e1,y+e2),(0,255,0),2)

    cv.imshow("Resultado",captura)


    if cv2.waitKey(1) == ord("q"):
        break

camara.release()
cv2.destroyAllWindows()
        

