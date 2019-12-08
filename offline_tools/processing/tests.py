
import pandas as pd
import pickle
# import cPiclke
import numpy as np
# from tinydb import TinyDB, Query, where
# from processing_functions import misc as msc
import time


t1 = {'with_terrain_veg': [{'checkpoint': '/home/kauevestena/Dropbox/data/checkpoints/deeplab_plus/0012/model.ckpt', 'image': '0359', 'accuracy': 0.7071266174316406, 'precision': 0.8746151429469055, 'recall': 0.2766663685240949, 'f1': 0.4203604297373408, 'iou': 0.26611161030072455}, {'checkpoint': '/home/kauevestena/Dropbox/data/checkpoints/deeplab_plus/0012/model.ckpt', 'image': '0437', 'accuracy': 0.612396240234375, 'precision': 0.48549038093274016, 'recall': 0.1637697146775588, 'f1': 0.24492070805404037, 'iou': 0.13954965406861042}], 'only_trees': [{'checkpoint': '/home/kauevestena/Dropbox/data/checkpoints/deeplab_plus/0012/model.ckpt', 'image': '0359', 'accuracy': 0.7330970764160156, 'precision': 0.8462142632736412, 'recall': 0.29274946471464125, 'f1': 0.4350073079935722, 'iou': 0.2779612391901096}, {'checkpoint': '/home/kauevestena/Dropbox/data/checkpoints/deeplab_plus/0012/model.ckpt', 'image': '0437', 'accuracy': 0.638092041015625, 'precision': 0.4577968947942138, 'recall': 0.16888932363841883, 'f1': 0.24674870980547836, 'iou': 0.14073778880727464}]}




# db = TinyDB(msc.joinToHome("Dropbox/data/tinydbs/validation/only_trees.json"))

# # print(db.all())

# imgname  = '0059'
# ckptname = '/home/kaue/Dropbox/data/checkpoints/deeplab_plus/0036/model.ckpt'

# for entry in db:
#     print(entry)

# print("{:.4f} test".format(1.3895432964532942378423786))

# print(len(db))


# import numpy as np

t2 = np.array([[1,2,3],[1,2,3],[1,2,3]])
t3 = pd.DataFrame(t2)

# t3.columns = ['a','b','c']
# t3.index = ['aa','bb','cc']

#### .loc['line','column']
# t3.loc['bb','b'] = 100


# print(t3.T)


# # df = pd.DataFrame(data, index=index, columns=columns)


l = ['abracadabra','bb','cc','abracadabra','baba','baca']
c = set()

for item in l:
    if 'a' in item:
        c.add(item)

print(len(c))

for item in c:
    print(item)

# print(c[0])

# import hashlib
# from processing_functions import misc as msc


# print(msc.shortHash(inputstring,6))

testEntry = t1['with_terrain_veg'][0]

print(list(testEntry.values()))


for i,key in enumerate(t1):
    print(i,key)

print(len(t1))

print('\n\n\n\n')

print(t3)

# /home/kauevestena/data/pickles

# t3.to_pickle("/home/kauevestena/data/pickles/t1.p",compression=None)



t1 = time.time()

pickle1_path = "/home/kauevestena/data/pickles/precisionwith_terrain_veg.p"

with open(pickle1_path,'rb') as pickled_file:
    df1 = pickle.load(pickled_file)

t2 = time.time()

print(t1-t2)

print(df1)

test_dict = {'a':'b','c':'d'}

# with open("pickletest.pickle",'wb') as test_pickle:
#     pickle.dump(test_dict,test_pickle)

with open("pickletest.pickle",'rb') as recover_pickle:
    td2 = pickle.load(recover_pickle)

print(td2)