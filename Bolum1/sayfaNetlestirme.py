import cv2
import numpy as np

img = cv2.imread('sayfa.jpg',0)

ret,th1 = cv2.threshold(img,12,255,cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

cv2.imshow('orj',img)
cv2.imshow('th1',th1)
cv2.imshow('gaus',gaus)

cv2.waitKey()