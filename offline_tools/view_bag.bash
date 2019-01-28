#!/bin/bash

xterm -hold -e roscore &

sleep 5

source /home/kaue/kalibr_workspace/devel/setup.bash

bagpath=$(head -n 1 $HOME/snav/configurations/current_bag.txt)

rosbag play $bagpath &

sleep 2

#xterm -hold -e 
rosrun image_view image_view image:=/camera1/image_raw &

#xterm -hold -e 
rosrun image_view image_view image:=/camera2/image_raw &