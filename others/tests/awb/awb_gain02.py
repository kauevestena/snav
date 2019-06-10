from time import sleep
from fractions import Fraction
from picamera import PiCamera

def print_awb_gains(g):
    print([float(g[0]),float(g[1])])
    sleep(5)

basePath = "/home/ubuntu/snav_ws/snav/others/tests/awb/"

camera = PiCamera(resolution=(1280, 720), framerate=30)

camera.shutter_speed = 100000

camera.exposure_mode = "auto"

camera.iso = 100

sleep(2)

r_gain = 0.6
b_gain = 1.18

# r_gain = 2
# b_gain = 4

camera.awb_mode = 'off'
camera.awb_gains = (Fraction(r_gain),Fraction(b_gain))
sleep(2)
print(print_awb_gains(camera.awb_gains))
print(camera.exposure_speed)
print(camera.shutter_speed)
print(float(camera.digital_gain))
print(float(camera.analog_gain))

camera.capture(basePath+"test.jpeg")