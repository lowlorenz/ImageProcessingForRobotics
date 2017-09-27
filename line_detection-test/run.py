import cv2
import numpy as np
import time
from matplotlib import pyplot as plt

blue  = True
red   = True
green = True


blue_trigger  = 45
red_trigger   = 45
green_trigger = 45


def cleverSearch(img,b,trigger,color):
    i = 0
    while 480 > i:
        turn = False
        j = 0
        while 640 > j:
            if(b.item(i,j) < trigger):
                img.itemset((i,j,color),255)
                if turn :
                    j -= 3
                    turn = False
                else:
                    j += 1
            else:
                j += 4
                turn = True
        i += 1


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

        cleverSearch(img,b,red_trigger,0)

        cv2.imshow('redOnly', img)

    if green:
        #copy to work on
        img = np.array(frame, copy=True)

        #delete red and blue
        img[:,:,2] = 0
        img[:,:,0] = 0

        cleverSearch(img,b,green_trigger,2)

        cv2.imshow('greenOnly', img)

    if blue:
        #copy to work on
        img = np.array(frame, copy=True)

        #delete red and green
        img[:,:,1] = 0
        img[:,:,2] = 0

        cleverSearch(img,b,blue_trigger,1)

        cv2.imshow('blueOnly', img)

    print 'processing took {} s'.format(time.time() - last)
    last = time.time()

    if cv2.waitKey(1) == ord('q'):
        break
