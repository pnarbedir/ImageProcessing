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

    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask,kernel,iterations = 1)
    dilation = cv2.dilate(mask,kernel,iterations = 1)

    closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
    opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)

    cv2.imshow('sonresim',son_resim)
    cv2.imshow('erosion',erosion)
    cv2.imshow('dilation',dilation)
    cv2.imshow('closing',closing)
    cv2.imshow('opening',opening)

    if cv2.waitKey(50) & 0xFF == ord('q'):
       break
kamera.release()