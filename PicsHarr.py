# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 21:07:34 2015

@author: ABDULLAH A. ABUOLAIM
"""

import cv2
import numpy as np

img = cv2.imread('Soccer-left.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img1 = cv2.imread('Soccer-mid.jpg')
gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

img2 = cv2.imread('Soccer-right.jpg')
gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)

gray1 = np.float32(gray1)
dst1 = cv2.cornerHarris(gray1,2,3,0.04)

gray2 = np.float32(gray2)
dst2 = cv2.cornerHarris(gray2,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)
dst1 = cv2.dilate(dst1,None)
dst2 = cv2.dilate(dst2,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]
img1[dst1>0.01*dst1.max()]=[0,0,255]
img2[dst2>0.01*dst2.max()]=[0,0,255]

cc=img[250:400,1050:1250,:]
cv2.imshow('cut',cc)
cv2.imshow('dst',img)
cv2.imshow('dst1',img1)
cv2.imshow('dst2',img2)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()