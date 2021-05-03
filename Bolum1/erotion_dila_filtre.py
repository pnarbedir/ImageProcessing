import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('j.png')
img2 = cv2.imread('j2.png')
img3 = cv2.imread('j3.png')

kernel = np.ones((2,2),np.uint8)
erotion = cv2.erode(img2,kernel,iterations=1)
dilation= cv2.dilate(img3,kernel,iterations=1)

plt.subplot(321),plt.imshow(img1), plt.title('orj')
plt.xticks([]), plt.yticks([])
plt.subplot(322),plt.imshow(img1), plt.title('orj')
plt.xticks([]), plt.yticks([])
plt.subplot(323),plt.imshow(img2), plt.title('j2')
plt.xticks([]), plt.yticks([])
plt.subplot(324),plt.imshow(erotion), plt.title('ero')
plt.xticks([]), plt.yticks([])
plt.subplot(325),plt.imshow(img3), plt.title('j3')
plt.xticks([]), plt.yticks([])
plt.subplot(326),plt.imshow(dilation), plt.title('dila')
plt.xticks([]), plt.yticks([])

plt.show()