import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('original.jfif',0)
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

blur = cv2.GaussianBlur(img,(5,5),0)
ret,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('orj',img)
cv2.imshow('th1',th1)
cv2.imshow('th2',th2)
cv2.imshow('th3',th3)

cv2.waitKey()
