#!/bin/bash


#### usage:
######## bash topic_extractor.bash <optional_suffix>

# bagpath=$(head -n 1 /home/kauevestena/snav/configurations/current_bag.txt)
bagpath="/home/kauevestena/data/2019-06-05-15-17-41.bag"

# echo $HOME
# echo $1
rostopic echo -b $bagpath -p imu/data/orientation > $HOME/data/orientation$2.csv
rostopic echo -b $bagpath -p imu/data/angular_velocity > $HOME/data/angular_velocity$2.csv
rostopic echo -b $bagpath -p imu/data/linear_acceleration > $HOME/data/linear_acceleration$2.csv