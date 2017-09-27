import cv2
import numpy as np
import time
from matplotlib import pyplot as plt



cam = cv2.VideoCapture(0)
time.sleep(1)
ret, frame = cam.read(0)
time.sleep(1)
ret, frame = cam.read(0)
time.sleep(1)
ret, frame = cam.read(0)
cv2.imwrite('test/no_averaging.png',frame)
cv2.imwrite('test/averaging.png',cv2.blur(frame,(5,5)))
cam.release()
cv2.destroyAllWindows()
