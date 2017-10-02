import cv2
import numpy
import time

cam = cv2.VideoCapture(0)
last = time.time()
print 'start'
print cv2.useOptimized()
while True:
    ret, frame = cam.read(0)

    # Now create a mask of logo and create its inverse mask also
    img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(img,(5,5),0)
    ret,res  = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)


    cv2.imshow('img2gray',res)
    print 'time : {}'.format(time.time()-last)
    last = time.time()

    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()
cam.release()
