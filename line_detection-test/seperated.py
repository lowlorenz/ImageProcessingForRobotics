import cv2
import numpy as np
import time
from matplotlib import pyplot as plt

blue = True
red  = True
green = True

div = 2

cam = cv2.VideoCapture(0)
print 'camera resolution {}x{}'.format(cam.get(cv2.CAP_PROP_FRAME_WIDTH ),cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

last = time.time()

while True :
    ret, frame = cam.read(0)
    frame = cv2.GaussianBlur(frame,(5,5),0)
    b,g,r = cv2.split(frame)

    if red:
        #copy to work on
        img = np.array(frame, copy=True)

        #delete blue and green
        img[:,:,1] = 0
        img[:,:,0] = 0

        for i in range(len(b)/div):
            for j in range(len(b[0])/div):
                if(b[i*div][j*div] < 30):
                    img.itemset((i*div,j*div,0),255)

        cv2.imshow('redOnly', img)

    if green:
        #copy to work on
        img = np.array(frame, copy=True)

        #delete red and blue
        img[:,:,2] = 0
        img[:,:,0] = 0

        for i in range(len(b)/div):
            for j in range(len(b[0])/div):
                if(b[i*div][j*div] < 30):
                    img.itemset((i*div,j*div,2),255)

        cv2.imshow('greenOnly', img)

    if blue:
        #copy to work on
        img = np.array(frame, copy=True)

        #delete red and green
        img[:,:,1] = 0
        img[:,:,2] = 0

        for i in range(len(b)/div):
            for j in range(len(b[0])/div):
                if(b[i*div][j*div] < 30):
                    img.itemset((i*div,j*div,1),255)

        cv2.imshow('blueOnly', img)

    print 'processing took {} s'.format(time.time() - last)
    last = time.time()

    if cv2.waitKey(1) == ord('q'):
        break
