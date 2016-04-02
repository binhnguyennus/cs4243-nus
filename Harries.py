import cv2
import numpy as np
import time
import math


cap = cv2.VideoCapture('football_right.mp4')

start = time.localtime(time.time()).tm_sec
img1=cv2.imread('Soccer-left.jpg')
img2=cv2.imread('Soccer-mid.jpg')
img3=cv2.imread('Soccer-right.jpg')
print img1.shape
print img2.shape
print img3.shape
while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,3,0.04)
    y=dst

#result is dilated for marking the corners, not important
    dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
    frame[dst>0.01*dst.max()]=[0,0,255]

    cv2.imshow('dst',frame)
#cv2.imwrite('3.jpg',img)

    tim_diff=time.localtime(time.time()).tm_sec
    tim_diff=math.fabs(tim_diff-start)

    if cv2.waitKey(1) & 0xFF == 27 or tim_diff>30:
        break

print y.shape

cap.release()
cv2.destroyAllWindows()