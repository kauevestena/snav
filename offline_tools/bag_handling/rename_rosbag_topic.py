#!/usr/bin/python
import os


with open(os.environ['HOME']+'/snav/configurations/current_bag.txt') as f:
   	bagpath = f.readline()

#original from: https://answers.ros.org/answers/13697/revisions/
#thanks Tim Field!

from rosbag import Bag
with Bag(os.environ['HOME']+'/rosbags/renamed.bag', 'w') as Y:
    for topic, msg, t in Bag(bagpath):
        Y.write('/imu0' if topic == 'imu/data' else topic, msg, t)

print "done"