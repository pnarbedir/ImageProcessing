import cv2
import numpy as np

kamera = cv2.VideoCapture(0)
while True:
    ret,frame = kamera.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    altdeger_kirmizi = np.array([150,30,30])
    ustdeger_kirmizi =np.array([190,255,255])

    mask = cv2.inRange(hsv,altdeger_kirmizi,ustdeger_kirmizi)
    son_resim = cv2.bitwise_and(frame,frame,mask=mask)

    blur = cv2.GaussianBlur(frame,(15,15),0)

    cv2.imshow('orjinal',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('sonresim',son_resim)
    cv2.imshow('blur',blur)
    if cv2.waitKey(50) & 0xFF == ord('q'):
       break
kamera.release()