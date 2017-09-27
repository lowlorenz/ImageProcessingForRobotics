import cv2
import numpy as np
import time
from matplotlib import pyplot as plt

def raster(img):
    for i in range (15):
        img = cv2.line(img,(0,i*32),(640,i*32),(0,0,0),1)
    for i in range (20):
        img = cv2.line(img,(i*32,0),(i*32,480),(0,0,0),1)
    return img



cam = cv2.VideoCapture(0)
print 'camera resolution {}x{}'.format(cam.get(cv2.CAP_PROP_FRAME_WIDTH ),cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True :
    ret, frame = cam.read(0)

    frame = cv2.GaussianBlur(frame,(5,5),0)

    frame0 = np.array(frame, copy=True)
    frame1 = np.array(frame, copy=True)
    frame2 = np.array(frame, copy=True)

    frame0[:,:,0] = 0
    frame0[:,:,1] = 0
    frame1[:,:,1] = 0
    frame1[:,:,2] = 0
    frame2[:,:,2] = 0
    frame2[:,:,0] = 0


    trigger = 20
    b,g,r = cv2.split(frame)


    for i in range(len(b)):
        for j in range(len(b[0])):
            if(b[i][j] < 20):
                frame2.itemset((i,j,2),255)


    cv2.imshow('pic0', frame2)
#    cv2.imshow('pic1', frame1)
#    cv2.imshow('pic2', frame2)





    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
