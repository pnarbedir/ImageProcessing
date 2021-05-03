import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('kosebul.jpg')
gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gri = np.float32(gri)

koseler = cv2.goodFeaturesToTrack(gri,80,0.01,10)
koseler = np.int0(koseler)

for kose in koseler:
    x,y = kose.ravel()
    cv2.circle(img,(x,y),3,255,-1)
cv2.imshow('koseler',img)
cv2.waitKey(0)