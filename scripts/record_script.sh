#!/bin/bash

source /home/ubuntu/snav_ws/devel/setup.bash

rosbag record /camera1/image_raw /camera2/image_raw imu/data &

/bin/bash