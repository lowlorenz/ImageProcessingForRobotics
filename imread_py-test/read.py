import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('test_pic7.png',0)
cv2.imshow('title',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
