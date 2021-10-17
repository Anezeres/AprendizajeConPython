import cv2
import numpy as np

def ordernarPuntos(puntos):
    nPuntos = np.concatenate([puntos[0],puntos[1],puntos[2],puntos[2]]).tolist()
    y = sorted(nPuntos,key=lambda nPuntos:nPuntos[1])
    x1 = y[0:2]
    x1 = sorted(x1,key=lambda x1: x1[0])
    x2 = y[2:4] 
    x2 = sorted(x2,key=lambda x2: x2[0])
    return [x1[0], x1[1],x2[0],x2[1]]

def alineamiento(imagen,ancho,alto):
    imagenAlineada = None
    grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    tipoUmbral,umbral = cv2.threshold(grises,150,255,cv2.THRESH_BINARY)
    cv2.imshow("Umbral",umbral) 
    contorno = cv2.findContours(umbral,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]

    contorno = sorted(contorno,key=cv2.contourArea, reverse=True)[:1]

    for c in contorno:
        epsilon = 0.01*cv2.arcLength(c,True)
        approx = cv2.approxPolyDP(c,epsilon,True)

        if len(approx)==4:
            puntos = ordernarPuntos(approx)
            puntos1 = np.float32(puntos)
            puntos2 = np.float32([[0,0],[ancho,0],[0,alto],[ancho,alto]])

            M = cv2.getPerspectiveTransform(puntos1,puntos2)
            imagenAlineada = cv2.warpPerspective(imagen,M, (ancho,alto) )
    return imagenAlineada

capturaVideo = cv2.VideoCapture(0)

while True:
    tipoCamara,camara = capturaVideo.read()

    if tipoCamara == False:
        break
    imagen_A6 = alineamiento(camara,ancho = 480, alto = 677)
    if imagen_A6 is not None:
        puntos = []
        imagenGris = cv2.cvtColor(imagen_A6,cv2.COLOR_BGR2GRAY)
        gauss = cv2.GaussianBlur(imagenGris,(5,5),1)
        _,Umbral2 = cv2.threshold(gauss,0,255,cv2.THRESH_OTSU+cv2.THRESH_BINARY_INV)
        cv2.imshow("Umbral",Umbral2)
        contorno2 = cv2.findContours(Umbral2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
        cv2.drawContours(imagen_A6,contorno2,-1,(0,255,0),2)

        suma1 = 0.0
        suma2 = 0.0

        for c2 in contorno2:
            area = cv2.contourArea(c2)
            momentos = cv2.moments(c2)

            if (momentos["m00"])==0:
                momentos["m00"]=1.0
            
            x = int(momentos["m10"]/momentos["m00"])
            y = int(momentos["m01"]/momentos["m00"])


            if area < 9300 and area>8000:
                font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
                cv2.putText(imagen_A6, "S/ 0.20",(x,y),font,0.75,(255,0,0),2)
                suma1 += 0.2 

            if area < 7800 and area>6500:
                font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
                cv2.putText(imagen_A6, "S/ 0.10",(x,y),font,0.75,(255,0,0),2)
                suma2 += 0.2 

        total = suma1 + suma2

        print(f"Sumatoria total en centimos: {round(total,2)} ")

        cv2.imshow("Imagen A6", imagen_A6)
        cv2.imshow("Camara",camara)

    if cv2.waitKey(1) == ord("q"):
        break

capturaVideo.release()
cv2.destroyAllWindows()

