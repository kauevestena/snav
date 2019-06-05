#!/bin/bash

source /home/ubuntu/snav_ws/devel/setup.bash

#configuring GPS
python /home/ubuntu/snav_ws/snav/utilitaries/gnss_config.py

sleep 5

#IMU DRIVER
xterm -hold -e roslaunch /home/ubuntu/snav_ws/src/ros_bno055_driver/launch/bosch_bno055_driver_notemp.launch &

sleep 5

#O+W ACCES FOR CAMERAS
# echo ubuntu | sudo -S chmod o+w /dev/bus/usb/001/004
echo ubuntu | sudo -S chmod o+w /dev/bus/usb/001/005

#O+W ACCES FOR GNSS RECEIVER
echo ubuntu | sudo -S chmod o+w /dev/ttyUSB0

#GNSS DRIVER
xterm -hold -e rosrun nmea_navsat_driver nmea_serial_driver _port:=/dev/ttyUSB0 _baud:=9600 &

sleep 5

#CAMERAS DRIVER
xterm -hold -e roslaunch $HOME/snav_ws/snav/launchfiles/logi_cam.xml &
xterm -hold -e roslaunch $HOME/snav_ws/snav/launchfiles/camerav2_1280x960.launch &

echo "fim"


/bin/bash