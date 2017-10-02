import numpy
import cv2
import time


cam = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 4.0, (640,480))

last = time.time()
while cam.isOpened():
    try:

        ret, frame = cam.read()

        if ret:
            out.write(frame)
            print 'processing took {} s'.format(time.time() - last)
            last = time.time()

        else:
            break
    except KeyboardInterrupt:
        cam.release()
        out.release()
        exit()

cam.release()
out.release()
