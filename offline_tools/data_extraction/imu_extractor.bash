#!/bin/bash


#### usage:
######## bash topic_extractor.bash <optional_suffix>

# bagpath=$(head -n 1 /home/kauevestena/snav/configurations/current_bag.txt)
bagpath="/home/kaue/data/rosbags/2019-06-13-15-43-38.bag"

# echo $HOME
# echo $1
rostopic echo -b $bagpath -p imu/data/orientation > $HOME/data/orientation$1.csv
rostopic echo -b $bagpath -p imu/data/angular_velocity > $HOME/data/angular_velocity$1.csv
rostopic echo -b $bagpath -p imu/data/linear_acceleration > $HOME/data/linear_acceleration$1.csv