import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gul.jpg')
median = cv2.medianBlur(img, 5)
cv2.imshow('Result', img)
cv2.imshow('Result2', median)

cv2.waitKey(0)
cv2.destroyAllWindows