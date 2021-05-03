import cv2
import numpy as np

img = cv2.imread('insan.jpg')
body_cascade = cv2.CascadeClassifier('fulbody.xml')

griton = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
bodies = body_cascade.detectMultiScale(griton,1.8,2)

for(x,y,w,h) in bodies:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow('body',img)
    cv2.waitKey(0)