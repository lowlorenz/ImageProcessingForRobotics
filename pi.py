from picamera import PiCamera
import time

camera = PiCamera()
camera.resolution = (1024,768)

camera.start_preview()
time.sleep(2)
camera.capture('test/test.jpeg')

camera.start_recording('test/test.h264')
time.sleep(60)
camera.stop_recording()

exit()
