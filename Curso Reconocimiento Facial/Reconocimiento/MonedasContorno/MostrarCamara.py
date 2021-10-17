import cv2

capturarVideo = cv2.VideoCapture(0)

if (not capturarVideo.isOpened()):
    print("No se encontró una camara")
    exit()

while True:
    _,camara = capturarVideo.read()
    grises = cv2.cvtColor(camara,cv2.COLOR_BGR2GRAY)

    cv2.imshow("Envivo",grises)
    if cv2.waitKey(1) == ord("q"):
        break

capturarVideo.release()
cv2.destroyAllWindows()
