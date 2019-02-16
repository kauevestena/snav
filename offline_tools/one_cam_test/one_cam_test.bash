#!/bin/bash

source $HOME/catkin_ws/devel/setup.bash

roscore &

sleep 2

#O+W ACCES FOR CAMERAS
echo $1 | sudo -S chmod o+w /dev/bus/usb/001/004
echo $1 | sudo -S chmod o+w /dev/bus/usb/001/005
echo $1 | sudo -S chmod o+w /dev/bus/usb/001/013
echo $1 | sudo -S chmod o+w /dev/bus/usb/001/012

# rosbag record --buffsize 1 --chunksize 32 camera1/image_raw

roslaunch $HOME/snav/offline_tools/one_cam_test/one_cam.xml