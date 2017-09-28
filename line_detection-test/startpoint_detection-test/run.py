import cv2
import time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


trigger  = 40

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
            img = cv2.rectangle(img,(j*16,i*16),(j*16+16,i*16+16),(0,blobs[i][j]*5,0),1)
    return img,blobs

def plotColor(b):
    fig = plt.figure()
    ax = Axes3D(fig)
    X = np.arange(0,40)
    Y = np.arange(0,30)
    X,Y = np.meshgrid(X,Y)

    for x in np.nditer(blobs):
        if x > 10:
            x = 400
        else:
            x = 0


    ax.plot_surface(X,Y,b,rstride = 1,cstride = 1,cmap = 'hot')

    plt.show()



cam = cv2.VideoCapture(0)
print 'camera resolution {}x{}'.format(cam.get(cv2.CAP_PROP_FRAME_WIDTH ),cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

last = time.time()
counter = 10

print 'started'

while True :
    ret, frame = cam.read(0)
    b,g,r = cv2.split(frame)


    frame ,blobs = blobAnaylsisViaCleversearch(frame,b,trigger,0)
    cv2.imshow('Blue', frame)

    if counter == 0:
        print 'processing took {} s'.format((time.time() - last)/1000)
        plotColor(blobs)
        last = time.time()
        counter = 100

    counter -= 1

    if cv2.waitKey(1) == ord('q'):
        break
