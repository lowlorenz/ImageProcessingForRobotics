import cv2
import numpy as np
import time
from matplotlib import pyplot as plt

trigger  = 34

def blobAnaylsisViaCleversearch(img,b,trigger,color):
    blobs = np.zeros((30,40))
    i = 0
    while 480 > i:
        turn = False
        j = 0
        while 640 > j:
            if(b.item(i,j) < trigger):
                #img.itemset((i,j,color),255)
                blobs[int(i/16)][int(j/16)] += 1
                if turn :
                    j -= 3
                    turn = False
                else:
                    j += 1
            else:
                j += 4
                turn = True
        i += 1

    for i in range (30):
        for j in range (40):
            if blobs[i][j] > 20:
                img = cv2.rectangle(img,(j*16,i*16),(j*16+16,i*16+16),(0,255,0),2)
    return img

cam = cv2.VideoCapture(0)
print 'camera resolution {}x{}'.format(cam.get(cv2.CAP_PROP_FRAME_WIDTH ),cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

last = time.time()
counter = 100

print 'started'

while True :
    ret, frame = cam.read(0)
    frame = cv2.GaussianBlur(frame,(5,5),0)
    b,g,r = cv2.split(frame)

    frame = blobAnaylsisViaCleversearch(frame,b,trigger,0)
    cv2.imshow('redOnly', frame)

    if counter == 0:
        print 'processing took {} s'.format((time.time() - last)/1000)
        last = time.time()
        counter = 100

    counter -= 1

    if cv2.waitKey(1) == ord('q'):
        break
