#!/bin/bash


#### usage:
######## bash topic_extractor.bash <topic_name> <outname>

# bagpath=$(head -n 1 /home/kauevestena/snav/configurations/current_bag.txt)
bagpath="/home/kauevestena/Dropbox/data/covs_from_bag/2019-05-17-17-13-18.bag"

# echo $HOME
echo $1
rostopic echo -b $bagpath $1 > $HOME/data/$2.csv