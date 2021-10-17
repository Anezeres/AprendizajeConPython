import cv2
from cv2 import cvtColor
import numpy as np

path = r'D:\Mis Documentos\Desktop\Python\Curso Python 1\Curso Reconocimiento Facial\Reconocimiento\MonedasContorno\monedas.jpg'

valorGauss = 3
valorKernel = 3

original = cv2.imread(path)
grises = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
gauss = cv2.GaussianBlur(grises,(valorGauss,valorGauss),0)
canny = cv2.Canny(gauss, 60,100)

kernel = np.ones((valorKernel,valorKernel), np.uint8)
cierre = cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernel)

contornos,jerarquia = cv2.findContours(cierre.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

print(f"Monedas encontradas: {len(contornos)}")
cv2.drawContours(original,contornos,-1,(0,255,0),5)

#Mostrar resultado

#cv2.imshow("Grises",grises)
#cv2.imshow("Gauss",gauss)
#cv2.imshow("Canny",canny)
#cv2.imshow("Cierre",cierre)
cv2.imshow("Resultado",original)
cv2.waitKey(0)
cv2.destroyAllWindows()