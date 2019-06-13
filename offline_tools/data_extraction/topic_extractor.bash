#!/bin/bash


#### usage:
######## bash topic_extractor.bash <topic_name> <outname>

# bash topic_extractor.bash /camera1/image_raw/compressed logicam.txt

# bagpath=$(head -n 1 /home/kauevestena/snav/configurations/current_bag.txt)
bagpath="/home/kaue/Dropbox/data/2019-06-05-19-04-47.bag"

# echo $HOME
mkdir $HOME/data

rosbag info $bagpath

echo $1
rostopic echo -b $bagpath -p $1 > $HOME/data/$2.csv