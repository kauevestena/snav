#!/bin/bash

source /home/ubuntu/snav_ws/devel/setup.bash

# rosbag record /camera1/image_raw /camera2/image_raw imu/data /fix &

# rosbag record /camera1/image_raw/compressed /camera2/image_raw/compressed imu/data /fix &

rosbag record /camera1/image_raw /raspicam_node/image imu/data /fix &

/bin/bash