import cv2
import numpy

img1 = cv2.imread('gul.jpg')
img2 = cv2.imread('gul2.jpg')
cv2.imshow('a',img1)
cv2.imshow('b',img2)

#toplam = img1 + img2
toplam = cv2.addWeighted(img1,0.4,img2,0.6,0)
cv2.imshow('toplam', toplam)

cv2.waitKey()
cv2.destroyAllWindows()
