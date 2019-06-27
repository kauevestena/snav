#!/bin/bash

# bagpath=$(head -n 1 /home/kauevestena/snav/configurations/current_bag.txt)

bagpath=$1

# echo $HOME

rostopic echo -b $bagpath -p /fix > $HOME/data/gnss$2.csv