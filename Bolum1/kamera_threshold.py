import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('paletgri.jpg')
ret,thresh1= cv2.threshold(img,120,255,cv2.THRESH_BINARY)
ret,thresh2= cv2.threshold(img,120,255,cv2.THRESH_BINARY_INV)
ret,thresh3= cv2.threshold(img,120,255,cv2.THRESH_TRUNC)
ret,thresh4= cv2.threshold(img,120,255,cv2.THRESH_TOZERO)
ret,thresh5= cv2.threshold(img,120,255,cv2.THRESH_TOZERO_INV)

basliklar = ['orijinal','THRESH_BINARY','THRESH_BINARY_INV','THRESH_TRUNC','THRESH_TOZERO','THRESH_TOZERO_INV']
resimler = [img,thresh1,thresh2,thresh3,thresh4,thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(resimler[i],'gray')
    plt.title(basliklar[i])
    plt.xticks([]), plt.yticks([])
plt.show()