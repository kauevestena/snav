#!/bin/bash

source /home/ubuntu/snav_ws/devel/setup.bash

rosnode kill $(rosnode list | grep driver)
rosnode kill $(rosnode list | grep raspicam)

killall xterm