import cv2
import time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

cam = cv2.VideoCapture(0)
#cam.set(cv2.CAP_PROP_FRAME_WIDTH,320);
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT,240);
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 10.0, (640,480))

frame_count = 0

last = time.time()
print 'started'
while cam.isOpened():
    try:
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray,100,200)

        lines = cv2.HoughLines(edges,1,np.pi/180,60)

        x_long = 0
        y_long = 0
        x_line = [(0,0),(0,0)]
        y_line = [(0,0),(0,0)]

        if lines != None:
            print 'lines : {}'.format(len(lines))
            for line in lines:
                for rho,theta in line:
                    a = np.cos(theta)
                    b = np.sin(theta)
                    x0 = a*rho
                    y0 = b*rho
                    x1 = int(x0 + 1000*(-b))
                    y1 = int(y0 + 1000*(a))
                    x2 = int(x0 - 1000*(-b))
                    y2 = int(y0 - 1000*(a))

                    #print '{},{}'.format((x0,y0),(x1,y1))

                    if(abs(x1-x0) > x_long):
                        x_long = abs(x1-x0)
                        x_line = [(x0,y0),(x1,y1)]

                    if(abs(y1-y0) > y_long):
                        y_long = abs(y1-y0)
                        y_line = [(x0,y0),(x1,y1)]

        print 'max : {},{}'.format(x_long,y_long)

        cv2.line(frame,x_line[0],x_line[1],(0,0,255),2)
        cv2.line(frame,y_line[0],y_line[1],(0,0,255),2)


        #plt.plot(122),plt.imshow(edges,cmap = 'gray')
        #plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        #plt.show()

        #blur = cv2.GaussianBlur(frame,(5,5),0)
        #ret3,img = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

        if ret:
            frame_count += 1
            out.write(frame)
            print 'processing took {} s - u got {} frames '.format(time.time() - last,frame_count)
            last = time.time()

        else:
            break
    except KeyboardInterrupt:
        cam.release()
        out.release()
        exit()

cam.release()
out.release()
