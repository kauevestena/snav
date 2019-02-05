#!/bin/bash

roscore &

sleep 2

#O+W ACCES FOR CAMERAS
echo $1 | sudo -S chmod o+w /dev/bus/usb/001/004
# echo $1 | sudo -S chmod o+w /dev/bus/usb/001/005

roslaunch /home/kauevestena/snav/offline_tools/one_cam_test/one_cam.xml