import cv2
cam = cv2.VideoCapture(0)

for i in range(1000):
    ret, frame = cam.read(0)
    cv2.imwrite('pictures/test_pic{}.png'.format(i),frame)
cam.release()
