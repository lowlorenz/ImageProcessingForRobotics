import cv2
import numpy as np
import time

img = cv2.imread('test_pic408.png',0)
ret,thresh = cv2.threshold(img,40,255,cv2.THRESH_BINARY)
im2,contours,hierarchy = cv2.findContours(thresh, 1, 2)
thresh = cv2.bitwise_not(thresh)

for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)
    thresh = cv2.rectangle(thresh,(x,y),(x+w,y+h),255,2)

while True:
    cv2.imshow('center',thresh)

    if cv2.waitKey(1) == ord('q'):
        break


cv2.destroyAllWindows()
