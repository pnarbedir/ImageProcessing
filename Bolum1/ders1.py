import cv2
import numpy as np
from matplotlib import pyplot as plt
r = cv2.imread('gri-renk-paleti.jpg',0)
cv2.imshow('r',r)
cv2.imwrite('paletgri.jpg',r)
resim = np.zeros((400,400,3), dtype='uint8')
cv2.rectangle(resim,(100,100),(200,200),(255,1,1),2)
cv2.line(resim,(100,100),(200,200),(0,0,255),5)
cv2.circle(resim,(300,300),50,(0,255,0),5)
cv2.putText(resim,'pinos',(0,400),cv2.FONT_HERSHEY_DUPLEX,3,(255,0,0),5,cv2.LINE_4)


img = cv2.imread('lale.jpg')

print(str(img.item(200,200,1)))
img.itemset((300,300,0),200)

print(str(len(img.shape)))
print(str(img.shape[0]))
ROI = img[0:200,400:500]
cv2.imshow('roi', ROI)
img[100:300,100:200] = ROI

replicate = cv2.copyMakeBorder(img,20,20,50,50,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img,30,30,30,30,cv2.BORDER_REFLECT)
wrap = cv2.copyMakeBorder(img,30,30,30,30,cv2.BORDER_WRAP)
cv2.imshow('replicate',wrap)
cv2.imshow('Res',img)
print(img[500,500])
img[500,500] = [200,200,200]
cv2.rectangle(img,(0,0), (200,200),(0,0,255),5)
img[0:100,200:400] = [0,0,255]
cv2.imshow('rect', img)

cv2.imshow('res',resim)
cv2.waitKey(0)

