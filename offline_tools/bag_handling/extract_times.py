#!/usr/bin/python
import os


with open(os.environ['HOME']+'/snav/configurations/current_bag.txt') as f:
   	bagpath = f.readline()

bagpath = "/home/kauevestena/Downloads/MH_01_easy.bag"

#original from: https://answers.ros.org/answers/13697/revisions/
#thanks Tim Field!

file = open(os.environ['HOME']+"/data/times.csv",'w')

from rosbag import Bag

ns1 = 0

for topic, msg, t in Bag(bagpath):
    file.write(str(topic)+","+str(t.secs)+","+str(t.nsecs)+","+str(t.nsecs-ns1)+'\n')
    ns1 = t.nsecs

print "done"