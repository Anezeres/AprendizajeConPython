import cv2
import numpy as np

def ordernarPuntos(puntos):
    nPuntos = np.concatenate(puntos[0],puntos[1],puntos[2],puntos[2]).tolist()
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
    contorno, jerarquia = cv2.findContours(umbral,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]

    contorno = sorted(contornos,key=cv2.contourArea(), reverse=True)[:1]

    for c in contorno:
        epsilon = 0.01*cv2.arcLength(c,True)
        approx = cv2.approxPolyDP(c,epsilon,True)

        if len(approx)==4:
            puntos = ordernarPuntos(approx)
            puntos1 = np.float32(puntos)
            puntos2 = np.float32([[0,0],[ancho,0],[0,alto],[ancho,alto]])

            M = cv2.getPerspectiveTransform(puntos1,puntos2)
            imagenAlineada = cv2.warpPerspective(imagen,M, (ancho,alto) )