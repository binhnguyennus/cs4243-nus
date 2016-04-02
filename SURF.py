# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 08:22:36 2015

@author: ABDULLAH A. ABUOLAIM
"""

import numpy as np
import cv2
import time
import math

cap = cv2.VideoCapture('football_left.mp4')
cap1 = cv2.VideoCapture('football_mid.mp4')
cap2 = cv2.VideoCapture('football_right.mp4')
start = time.localtime(time.time()).tm_sec
surf = cv2.SURF()
while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    kp, des = surf.detectAndCompute(gray,None)
    
    img=cv2.drawKeypoints(gray,kp,None,(255,0,0),4)
    
    cv2.imshow('frame',img)
    #cv2.imshow('frame1',gray1)
    #cv2.imshow('frame2',gray2)
    tim_diff=time.localtime(time.time()).tm_sec
    tim_diff=math.fabs(tim_diff-start)
    if cv2.waitKey(1) & 0xFF == ord('q') or tim_diff>20:
        break

cap.release()
cv2.destroyAllWindows()