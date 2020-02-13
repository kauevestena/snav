
# it must be run in python 2.7


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
import pyproj

def linterp(x0,x1,y0,y1,x):
    # print(x0,x1,y0,y1,x)
    if x1 - x0 < 0.00000000000000000000000001:
        return y0
    else:
        return y0 + (x-x0)*((y1-y0)/(x1-x0))

def lla_to_ecef(lat, lon, alt):
    # thx: https://gis.stackexchange.com/q/230160
    ecef = pyproj.Proj(proj='geocent', ellps='WGS84', datum='WGS84')
    lla =  pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')
    return pyproj.transform(lla, ecef, lon, lat, alt, radians=False)

def ecef_to_lla(x,y,z):
    # thx: https://gis.stackexchange.com/q/230160
    ecef = pyproj.Proj(proj='geocent', ellps='WGS84', datum='WGS84')
    lla =  pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')
    return pyproj.transform( ecef, lla, x,y,z , radians=False)
     


from geometry_msgs.msg import _TwistStamped

t1 = time.time()

# bagpath = "/home/kauevestena/data/rosbags/2019-07-11-16-21-46.bag"
bagpath = msc.joinToHome('data/rosbags/2019-07-11-16-21-46.bag')
print('opened',bagpath)

current_bag = Bag(bagpath)

# print(current_bag.get_type_and_topic_info())

messages = current_bag.read_messages()

t0 = messages.next().timestamp.to_sec()

topic_names = {
    "imu" : "imu/data",
    "img" : "/raspicam_node/image/compressed",
    "gnss" : "/fix"
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
    # print(t.to_sec())
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

# if os.path.isfile(pickle_outpath): 
if not os.path.isfile(pickle_outpath): 
    for i,time_img in enumerate(obs_times['img']):
        if i % 100 == 0:
            print(i)

        for j,time_imu in enumerate(obs_times['imu']):
            if j >= last_j:
                delta = time_imu - time_img 
                if delta > 0.0:
                    if j != 0:
                        deltas_ids['img_imu'].append((i,j-1,j,time_imu,time_img,delta))
                        last_j = j-1
                    else:
                        deltas_ids['img_imu'].append((i,j,j,time_imu,time_img,delta))
                        last_j = j
                    break

        for k,time_gnss in enumerate(obs_times['gnss']):
            print(k)
            if k >= last_k:
                delta = time_gnss - time_img 
                # print(delta)
                if delta > 0.0:
                    if k != 0:
                        deltas_ids['img_gnss'].append((i,k-1,k,time_gnss,time_img,delta))
                        last_k = k-1
                    else:
                        deltas_ids['img_gnss'].append((i,k,k,time_gnss,time_img,delta))
                        last_k = k
                    break

    with open(pickle_outpath,'wb') as indexes:
        pickle.dump(deltas_ids,indexes)
else:
    with open(pickle_outpath,'rb') as indexes:
        deltas_ids = pickle.load(indexes)

# print(deltas_ids)
print([len(deltas_ids[key]) for key in deltas_ids])
print("took "+str(time.time()-t1 ))


full_idx = {}
# if not os.path.isfile(pickle_2_outpath): 
#     with open(pickle_2_outpath,'wb') as indexes:
#         pickle.dump(deltas_ids,indexes)
# else:
#     with open(pickle_2_outpath,'rb') as indexes:
#         deltas_ids = pickle.load(indexes)

# for key in obs:
#     print('\n\n\n')
#     print(type(obs[key][0][1]))
#     print(key)
#     print('\n')
#     print(obs[key][0][1])

# print(len(obs['gnss']))
# print(deltas_ids['img_gnss'])


lx = 0
ly = 0
lz = 0

with open(msc.joinToHome('Dropbox/data/img_gnss.csv'),'w+') as outfile:
    for i,regtuple in enumerate(deltas_ids['img_gnss']):
        # 'f' is for "first", 'l'  is for "last"
        im = str(regtuple[0])+'.png'
        f = regtuple[1]
        l = regtuple[2]
        t1_ = obs['gnss'][l][1].header.stamp.to_sec()
        t0 =  obs['gnss'][f][1].header.stamp.to_sec()
        t = regtuple[3] - regtuple[5]

        p0 = lla_to_ecef(*(obs['gnss'][f][1].latitude,obs['gnss'][f][1].longitude,obs['gnss'][f][1].altitude))
        p1 = lla_to_ecef(*(obs['gnss'][l][1].latitude,obs['gnss'][l][1].longitude,obs['gnss'][l][1].altitude))

        x = linterp(t0,t1_,p0[0],p1[0],t) 
        y = linterp(t0,t1_,p0[1],p1[1],t)
        z = linterp(t0,t1_,p0[2],p1[2],t)

        p_interp = ecef_to_lla(x,y,z)

        print(p_interp)

        # remember that we are on python 2.x!!!
        outfile.write(im+','+str(f)+','+str(l)+','+str(t)+','+str(p_interp[0])+','+str(p_interp[1])+','+str(p_interp[2])+'\n')



print('took',time.time()-t1)


