#!/bin/bash

source /home/ubuntu/snav_ws/devel/setup.bash

# rosrun topic_tools relay raspicam_node/image raspicam_node2/image_raw
# rosrun topic_tools relay raspicam_node/camera_info raspicam_node2/camera_info

ROS_NAMESPACE=raspicam_node rosrun image_proc image_proc