#!/bin/bash

xterm -e roscore &

sleep 5

source $HOME/catkin_ws/devel/setup.bash

