#!/bin/bash

source /home/ubuntu/snav_ws/devel/setup.bash

#IMU DRIVER
xterm -hold -e roslaunch /home/ubuntu/snav_ws/src/ros_bno055_driver/launch/bosch_bno055_driver.launch &

sleep 5

#O+W ACCES FOR CAMERAS
echo ubuntu | sudo -S chmod o+w /dev/bus/usb/001/004
echo ubuntu | sudo -S chmod o+w /dev/bus/usb/001/005

#CAMERAS DRIVER
xterm -hold -e roslaunch /home/ubuntu/snav_ws/snav/launchfiles/cameras.xml &

echo "fim"


/bin/bash