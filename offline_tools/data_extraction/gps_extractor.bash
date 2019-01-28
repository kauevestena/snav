#!/bin/bash

bagpath=$(head -n 1 /home/kauevestena/snav/configurations/current_bag.txt)

# echo $HOME

rostopic echo -b $bagpath -p /fix > $HOME/data/gnss.csv