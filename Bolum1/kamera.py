import cv2
import numpy as np
from matplotlib import pyplot as plt
kamera = cv2.VideoCapture(0)
def scala(frame,percent=15):
    width = int(frame,shape[1]*percent/100)
    height = int(frame,shape[0]*percent/100)
    boyut = (width,height)
    return cv2.resize(frame,boyut,interpolation=cv2.INTER_AREA)
while True:
    ret,frame=kamera.read()
    cv2.imshow('goruntu',frame)
    kamera.release()
    cv2.waitKey(0)
