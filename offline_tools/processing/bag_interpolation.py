
# it must be ran in python 2.7


from processing_functions import misc as msc
import rospy
from rosbag import Bag
import time
import numpy as np
import pickle
# import json
import os
np.set_printoptions(precision=5)
np.set_printoptions(suppress=True)

t1 = time.time()

# bagpath = "/home/kauevestena/data/rosbags/2019-07-11-16-21-46.bag"
bagpath = msc.joinToHome('data/rosbags/2019-07-11-16-21-46.bag')

current_bag = Bag(bagpath)

# print(current_bag.get_type_and_topic_info())

messages = current_bag.read_messages()

t0 = messages.next().timestamp.to_sec()

topic_names = {
    "imu" : "imu/data",
    "img" : "/raspicam_node/image/compressed",
    "gnss" : "/vel"
}

# imu_list = []
# img_list = []
# gnss_list = []

# # # # the big dict that will store all the relevant data
pickle_outpath = os.path.join(msc.PICKLESPATH,msc.filenameFromPathWtithoutExt(bagpath)+'_idx.pickle')
pickle_2_outpath = os.path.join(msc.PICKLESPATH,msc.filenameFromPathWtithoutExt(bagpath)+'_full_idx.pickle')

# if not os.path.isfile(pickle_outpath): 
obs = {}

for key in topic_names:
    obs[key] = []

img_count = 0

for topic, msg, t in messages:
    for key in topic_names:
        if topic == topic_names[key]:
            if key == "img":
                obs[key].append((t.to_sec(),img_count))
                img_count += 1
            else:
                obs[key].append((t.to_sec(),msg))

print("took "+str(time.time()-t1 ))


#     with open(pickle_outpath,'wb') as relevant_bagdata:
#         pickle.dump(obs,relevant_bagdata)
# else:
#     with open(pickle_outpath,'rb') as relevant_bagdata:
#         obs = pickle.load(relevant_bagdata)

# img_indexes = [entry[1] for entry in obs['img']]

# img_times =

obs_times = {}
for key in obs:
    obs_times[key] = np.array([entry[0] for entry in obs[key]])
    print(obs_times[key].shape,key)
    # print(obs_times[key][0:3]-t0,key)

# min_img_imu = np.minimum(obs_times['img'],obs_times['imu'])


# print(min_img_imu)

deltas_ids = {'img_imu':[],'img_gnss':[]}

# print([len(item) for item in ])

last_j = 0
last_k = 0

if not os.path.isfile(pickle_2_outpath): 
    for i,time_img in enumerate(obs_times['img']):
        if i % 100 == 0:
            print(i)

        for j,time_imu in enumerate(obs_times['imu']):
            if j >= last_j:
                delta = time_imu - time_img 
                if delta > 0.0:
                    if j != 0:
                        deltas_ids['img_imu'].append((i,j-1,j))
                        last_j = j-1
                    else:
                        deltas_ids['img_imu'].append((i,j,j))
                        last_j = j
                    break

        for k,time_gnss in enumerate(obs_times['gnss']):
            if k >= last_k:
                delta = time_gnss - time_img 
                if delta > 0.0:
                    if k != 0:
                        deltas_ids['img_gnss'].append((i,k-1,k))
                        last_k = k-1
                    else:
                        deltas_ids['img_gnss'].append((i,k,k))
                        last_k = k
                    break

    with open(pickle_outpath,'wb') as indexes:
        pickle.dump(deltas_ids,indexes)
else:
    with open(pickle_outpath,'rb') as indexes:
        deltas_ids = pickle.load(indexes)

# # print(deltas_ids)
print([len(deltas_ids[key]) for key in deltas_ids])
print("took "+str(time.time()-t1 ))

# if not os.path.isfile(pickle_2_outpath): 


#     with open(pickle_2_outpath,'wb') as indexes:
#         pickle.dump(deltas_ids,indexes)
# else:
#     with open(pickle_2_outpath,'rb') as indexes:
#         deltas_ids = pickle.load(indexes)
