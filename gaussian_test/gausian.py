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
cv2.imwrite('test/no_gaussian.png',frame)
cv2.imwrite('test/gaussian_5x5.png',cv2.GaussianBlur(frame,(5,5),0))
cv2.imwrite('test/gaussian_7x7.png',cv2.GaussianBlur(frame,(7,7),0))
cv2.imwrite('test/gaussian_9x9.png',cv2.GaussianBlur(frame,(9,9),0))
cam.release()
cv2.destroyAllWindows()
