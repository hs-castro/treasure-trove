from picamera import PiCamera
from os import system
from time import sleep

camera = PiCamera()
camera.resolution = (1024, 768)

for i in range(40):
    camera.capture('image{0:04d}.jpg'.format(i))
    sleep(.1)

system('convert -delay 1 -loop 0 /home/pi/Desktop/Pictures/image*.jpg animation.gif')
print('done')


