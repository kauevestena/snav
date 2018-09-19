#!/bin/dash

xterm -hold -e cd ~./rosbags && rosbag record /camera1/image_raw /camera2/image_raw &