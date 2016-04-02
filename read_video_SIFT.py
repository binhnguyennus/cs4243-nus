import numpy as np
import cv2
import time
import math

print cv2.__version__

cap = cv2.VideoCapture('football_left.mp4')
cap1 = cv2.VideoCapture('football_mid.mp4')
cap2 = cv2.VideoCapture('football_right.mp4')
start = time.localtime(time.time()).tm_sec
while(cap.isOpened()):
    ret, frame = cap.read()
    ret1,frame1=cap1.read()
    ret2,frame2=cap2.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)   
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY) 
    
    sift = cv2.SIFT()
    kp = sift.detect(gray,None)

    img=cv2.drawKeypoints(gray,kp)
    
    cv2.imshow('frame',img)
    #cv2.imshow('frame1',gray1)
    #cv2.imshow('frame2',gray2)
    tim_diff=time.localtime(time.time()).tm_sec
    tim_diff=math.fabs(tim_diff-start)
    if cv2.waitKey(1) & 0xFF == ord('q') or tim_diff>30:
        break

cap.release()
cv2.destroyAllWindows()