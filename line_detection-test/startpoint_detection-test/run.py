import cv2
import time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

debug = False
trigger = 40



def blobAnaylsisViaCleversearch(img,b,trigger,color):
    blobs = np.zeros((30,40))
    zeilensprung = False
    i = 0
    while 480 > i:
        spaltensprung = False
        linieninhalt = False
        j = 0
        while 640 > j:
            if(b.item(i,j) < trigger):
                linieninhalt = True
                blobs[int(i/16)][int(j/16)] += 1
                if spaltensprung :
                    j -= 3
                    spaltensprung = False
                else:
                    j += 1
            else:
                j += 4
                spaltensprung = True
        if linieninhalt:
            if zeilensprung:
                i -= 3
                zeilensprung = False
            else :
                i += 1
        else:
            i += 4
            zeilensprung = True

    for i in range (30):
        for j in range (40):
            img = cv2.rectangle(img,(j*16,i*16),(j*16+16,i*16+16),(0,blobs[i][j]*10,0),1)
    return img,blobs

def drawRectWithBlobs(img, x, y, color = (0,255,0),width = 3):

    return cv2.rectangle(img,(x*16,y*16),(x*16+16,y*16+16),color,width)

#Mau
def stdAbweichung(list):
    erw = 0
    for i in list:
        erw += i
    erw /= len(list)
    sum = 0
    for i in list:
        sum += np.square(i - erw)
    sum /= len(list)
    return np.sqrt(np.sqrt(sum))

def drawVerticals(img, blobs, color = (255,255,0),thick = 3):

    for y in range(30):
        start_x = -1
        end_x = -1
        draw = False
        for x in range(40):
            if blobs[y][x] > 10:
                if not draw:
                    draw = True
                    start_x = x
            else:
                if draw:
                    end_x = x
                    img = cv2.line(img,(start_x*16,y*16),(end_x*16,y*16),color,thick)
                    draw = False
    return img


def calcRoute(img,blobs):
    #http://matheguru.com/stochastik/167-standardabweichung.html

    start = [0,0]
    for y in range(29,0,-1):
        x_avg = 0
        x_abweichung = 0
        diff = 0

        for x in range(40):
            if blobs[y][x] > 10:
                x_avg += x
                x_abweichung += x*x
                diff += 1
        if not diff == 0:
            start = [x_avg/diff,y]
            img = drawRectWithBlobs(img, start[0], start[1])

            #print "Start at {} with a failure of {}".format((x_avg/diff,30 - y),stdAbweichung(blobs[start[1]][:]))
            break

    # CARE INDEX !
    if start[1] < 1:
        return img

    goto = [0,0]
    for y in range(start[1]-1,0,-1):
        x_avg = 0
        diff = 0

        for x in range(40):
            if blobs[y][x] > 10:
                x_avg += x
                diff += 1
        if not diff == 0:
            goto = [x_avg/diff,y]
            img = drawRectWithBlobs(img, goto[0], goto[1],(0,0,255))
            #print "Go to {}".format((x_avg/diff,30 - y))
            break

    return img


cam = cv2.VideoCapture(0)
print 'camera resolution {}x{}'.format(cam.get(cv2.CAP_PROP_FRAME_WIDTH ),cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

last = time.time()
counter = 10

print 'started'

while True :
    ret, frame = cam.read(0)
    b,g,r = cv2.split(frame)

    frame, blobs = blobAnaylsisViaCleversearch(frame,b,trigger,0)
    img = drawVerticals(frame, blobs)
    #frame = calcRoute(frame,blobs)


    cv2.imshow('Blue', frame)


    if counter == 0 and debug:
        print 'processing took {} s'.format((time.time() - last)/1000)
        #plotColor(blobs)
        last = time.time()
        counter = 100

    counter -= 1
    time.sleep(0.02)
    if cv2.waitKey(1) == ord('q'):
        break
