import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gul.jpg')
kenarlar = cv2.Canny(img,120,200)

plt.subplot(121), plt.imshow(img,cmap= 'gray')
plt.title('orjinal'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(kenarlar,cmap= 'gray')
plt.title('kenarlar'), plt.xticks([]), plt.yticks([])
plt.show()