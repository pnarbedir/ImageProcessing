import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('anaresim.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
nesne = cv2.imread('parcaresim.jpg',0)

w,h = nesne.shape[::-1]
res = cv2.matchTemplate(imgray,nesne,cv2.TM_CCOEFF_NORMED)
threshold = 0.75
loc = np.where(res>threshold)

for n in zip(*loc[::-1]):
    cv2.rectangle(img,n,(n[0]+w,n[1]+h),(0,255,255),2)
cv2.imshow('bulunanresimler',img)
cv2.waitKey(0)
