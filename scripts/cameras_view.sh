#!/bin/dash


#xterm -hold -e 
rosrun image_view image_view image:=/camera1/image_raw &

sleep 5

#xterm -hold -e 
rosrun image_view image_view image:=/camera2/image_raw &

