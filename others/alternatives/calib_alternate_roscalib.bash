#!/bin/bash

source /home/ubuntu/snav_ws/devel/setup.bash

#run camera driver
roslaunch /home/ubuntu/snav_ws/snav/launchfiles/camerav2_1280x960_10fps.launch &

sleep 10

rosrun camera_calibration cameracalibrator.py --size 9x6 --square 0.03 image:=/raspicam_node/image camera:=raspicam_node --fix-aspect-ratio -k 2 --zero-tangent-dist

