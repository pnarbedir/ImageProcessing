import cv2
import numpy as np
from matplotlib import pyplot as plt

res = cv2.imread('sudoku.jpg',0)
res = cv2.medianBlur(res,5)

ret,th1 = cv2.threshold(res,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(res,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,17,2)
th3 = cv2.adaptiveThreshold(res,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,17,2)

basliklar = ['orjinal','basit thresh','mean_c','gaussian_c']
resimler = [res,th1,th2,th3]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(resimler[i],'gray')
    plt.title(basliklar[i])
    plt.xticks([]),plt.yticks([])
plt.show()