import cv2
from cv2 import cvtColor, findContours

path = r'D:\Mis Documentos\Desktop\Python\Curso Python 1\Curso Reconocimiento Facial\Reconocimiento\MonedasContorno\contorno.jpg'
imagen = cv2.imread(path)
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
_,umbral = cv2.threshold(grises,100,255,cv2.THRESH_BINARY)
contorno, jerarquia = cv2.findContours(umbral,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE )
cv2.drawContours(imagen,contorno,-1,(251,60,50),3)



#Esto es para mostrar
cv2.imshow("Imagen Original",imagen)
#cv2.imshow("Imagen en Grises",grises)
#cv2.imshow("Imagen en Umbral",umbral)
cv2.waitKey(0)
cv2.destroyAllWindows()