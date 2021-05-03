import cv2
import numpy as np
yuz_cascade = cv2.CascadeClassifier('haarcascad_frontalface.xml')
goz_cascade = cv2.CascadeClassifier('cascade_goz.xml')

kamera = cv2.VideoCapture(0)

while True:
    ret,goruntu = kamera.read()
    griton =cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)
    yuzler = yuz_cascade.detectMultiScale(griton,9.2,2)

    for(x,y,w,h) in yuzler:
        cv2.rectangle(goruntu,(x,y),(x+w,y+h),(255,0,0),2)
        roi_griton = griton[y:y+h,x:x+w]
        roi_renkli = goruntu[y:y+h,x:x+w]

        gozler = goz_cascade.detectMultiScale(roi_griton)
        for(ex,ey,ew,eh) in gozler:
            cv2.rectangle(roi_renkli,(ex,ey),(ex+ew,ey+eh),(25,30,9),2)
        cv2.imshow('goruntu',goruntu)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
kamera.release()


