import cv2
import numpy as np

cap=cv2.VideoCapture('insan_video.mp4')
human_cascade=cv2.CascadeClassifier('fullbody.xml')

while True:
    _,frame=cap.read()
    griton=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    insan=human_cascade.detectMultiScale(griton,1.3,4)

    for (x,y,w,h) in insan:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),3)
    cv2.imshow('insanlar',frame)
    if cv2.waitKey(30) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()