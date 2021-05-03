import cv2
import numpy as np

kamera = cv2.VideoCapture(0)
yuz_cascade =cv2.CascadeClassifier('haarcascad_frontalface.xml')

while(1):
    ret,frame = kamera.read()

    griton = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    yuzler = yuz_cascade.detectMultiScale(griton,1.3,4)

    for(x,y,w,h) in yuzler:
      cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

      cv2.imshow('orj',frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
kamera.release()


