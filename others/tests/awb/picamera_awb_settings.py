from time import sleep
from picamera import PiCamera

basePath = "/home/ubuntu/snav_ws/snav/others/tests/awb/"

def print_awb_gains(g,mode):
    print([float(g[0]),float(g[1]),camera.exposure_speed,mode])
    sleep(5)

camera = PiCamera(resolution=(1280, 720), framerate=30)
# Set ISO to the desired value
# camera.iso = 100
# # Wait for the automatic gain control to settle
# sleep(2)
# # Now fix the values
# # print(camera.shutter_speed)
# # print(camera.exposure_speed)
# # camera.shutter_speed = 100000
# # camera.exposure_mode = 'off'
# # g = camera.awb_gains
# # while True:
#     print_awb_gains(camera.awb_gains)
#     sleep(0.5)
# camera.awb_mode = 'off'
# camera.awb_gains = g
# Finally, take several photos with the fixed settings
# camera.capture_sequence(['image%02d.jpg' % i for i in range(10)])

camera.shutter_speed = 100000

camera.exposure_mode = "auto"

camera.iso = 100

sleep(2)

awb_modes = ['auto','sunlight','cloudy','shade','tungsten','fluorescent','incandescent','flash','horizon']

for mode in awb_modes:
    camera.awb_mode = mode
    # camera.capture(mode+".jpeg",bayer=False)
    camera.capture(basePath+"test.jpeg")
    print_awb_gains(camera.awb_gains,mode)
    camera.awb_mode = 'off'
    # sleep(3)