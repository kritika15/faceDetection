import cv2
import numpy as np
def nothing(x):
    pass
cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')  
cv2.namedWindow("frame")
cv2.createTrackbar("Neighbours","frame",5,20,nothing)
while(True):
    _, frame = cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    Neighbours=cv2.getTrackbarPos("Neighbours","frame")
    
    faces=face_cascade.detectMultiScale(gray,1.3,Neighbours)
#to create a rectangle for the faces
    for rect in faces:
        (x,y,w,h)=rect#create rectangle
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),5)
       
        eyes = eye_cascade.detectMultiScale(gray,1.3,Neighbours)  
        for (ex,ey,ew,eh) in eyes: 
            cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
    cv2.imshow('frame',frame)
    key=cv2.waitKey(1) & 0xff
    if key==27:
        break
cap.release()
cv2.destroyAllWindows()
