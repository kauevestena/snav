#!/bin/bash

source $HOME/catkin_ws/devel/setup.bash

# roscore &

echo $1 | sudo -S chmod o+w /dev/bus/usb/001/021

# sleep 5

roslaunch $HOME/snav/others/tests/alternate_drivers/for_logicam/usb-cam-v4l.launch