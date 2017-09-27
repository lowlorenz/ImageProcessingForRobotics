import cv2
import numpy as np
import time
from matplotlib import pyplot as plt

blue  = False
red   = True
green = False


blue_trigger  = 45
red_trigger   = 45
green_trigger = 45


def raster(img):
    for i in range (30):
        img = cv2.line(img,(0,i*16),(640,i*16),(0,0,0),1)
    for i in range (40):
        img = cv2.line(img,(i*16,0),(i*16,480),(0,0,0),1)
    return img



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
counter = 100

print 'started'

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

        cv2.imshow('redOnly', raster(img))

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

    if counter == 0:
        print 'processing took {} s'.format((time.time() - last)/1000)
        last = time.time()
        counter = 100

    counter -= 1

    if cv2.waitKey(1) == ord('q'):
        break
