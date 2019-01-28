#!/bin/bash

# bagpath=$(head -n 1 /home/kauevestena/snav/configurations/current_bag.txt)
bagpath="/home/kauevestena/Downloads/MH_01_easy.bag"

# echo $HOME
echo $1
rostopic echo -b $bagpath $1 > $HOME/data/$1.csv