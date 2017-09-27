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

blue = False
red = True
green = False



cam = cv2.VideoCapture(0)
print 'camera resolution {}x{}'.format(cam.get(cv2.CAP_PROP_FRAME_WIDTH ),cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

last = time.time()

while True :
    ret, frame = cam.read(0)

#    frame = cv2.GaussianBlur(frame,(5,5),0)

    if(blue):
        pass

    elif(green):
        pass

    elif(red):
        img = np.array(frame, copy=True)
        img[:,:,2] = 0
        img[:,:,0] = 0
        b,g,r = cv2.split(img)
        div = 2

        for i in range(len(b)/div):
            for j in range(len(b[0])/div):
                if(b[i*div][j*div] < 20):
                    img.itemset((i*div,j*div,2),255)

        cv2.imshow('pic2', img)

        print 'processing took {} seconds'.format(time.time() - last)
        last = time.time()
    if cv2.waitKey(1) == ord('q'):
        break

'''
    #frame0 = np.array(frame, copy=True)
    #frame1 = np.array(frame, copy=True)

    #frame0[:,:,0] = 0
    #frame0[:,:,1] = 0
    #frame1[:,:,1] = 0
    #frame1[:,:,2] = 0

    b,g,r = cv2.split(frame)

   #trigger = 20

    div = 2

    for i in range(len(b)/div):
        for j in range(len(b[0])/div):
            if(b[i*div][j*div] < 20):
                frame2.itemset((i*div,j*div,2),255)


#    cv2.imshow('pic0', frame2)
#    cv2.imshow('pic1', frame1)
    cv2.imshow('pic2', frame2)


    print 'processing took {} seconds'.format(time.time() - last)
    last = time.time()

'''
cam.release()
cv2.destroyAllWindows()
