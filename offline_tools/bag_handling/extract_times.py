#!/usr/bin/python
import os


with open(os.environ['HOME']+'/snav/configurations/current_bag.txt') as f:
   	bagpath = f.readline()

# bagpath = "/home/kauevestena/Downloads/MH_01_easy.bag"

#original from: https://answers.ros.org/answers/13697/revisions/
#thanks Tim Field!

file = open(os.environ['HOME']+"/data/times.csv",'w')

from rosbag import Bag

s1 = 0
ns1 = 0
min = 0

def cds(secs,nsecs):
    return float(secs)+float(nsecs)*1e-9

# TODO : command-line input
topic_name = "/camera1/image_raw/compressed"

for topic, msg, t in Bag(bagpath):
    if topic == topic_name:
        # file.write(str(topic)+","+str(t.secs)+","+str(t.nsecs)+","+str(t.nsecs-ns1)+'\n')
        file.write(str(t.secs)+","+str(t.nsecs)+","+str(cds(t.secs,t.nsecs)-cds(s1,ns1))+'\n')
        s1  = t.secs
        ns1 = t.nsecs

print "done"