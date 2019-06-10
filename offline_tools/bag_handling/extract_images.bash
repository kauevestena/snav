#!/bin/bash

source $HOME/catkin_ws/devel/setup.bash

bagpath=/home/kauevestena/Dropbox/data/2019-06-10-12-30-30.bag

cd /home/kauevestena/data/extracted_images/10_06
mkdir rgb
mkdir ngr

# decompressing first
rosrun image_transport republish compressed in:=camera1/image_raw raw out:=camera1/image &
rosrun image_transport republish compressed in:=raspicam_node/image raw out:=raspicam/image &

#run the extracting node
rosrun image_view image_saver _filename_format:='rgb/%04d.%s' image:=camera1/image &
rosrun image_view image_saver _filename_format:='ngr/%04d.%s' image:=raspicam/image &


sleep 5


rosbag play $bagpath
