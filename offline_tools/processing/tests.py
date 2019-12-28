
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
# c = set()

# for item in l:
#     if 'a' in item:
#         c.add(item)

# print(len(c))

# for item in c:
#     print(item)

# # print(c[0])

# # import hashlib
# # from processing_functions import misc as msc


# # print(msc.shortHash(inputstring,6))

# testEntry = t1['with_terrain_veg'][0]

# print(list(testEntry.values()))


# for i,key in enumerate(t1):
#     print(i,key)

# print(len(t1))

# print('\n\n\n\n')

# print(t3)

# # /home/kauevestena/data/pickles

# # t3.to_pickle("/home/kauevestena/data/pickles/t1.p",compression=None)



# t1 = time.time()

# pickle1_path = "/home/kauevestena/data/pickles/precisionwith_terrain_veg.p"

# with open(pickle1_path,'rb') as pickled_file:
#     df1 = pickle.load(pickled_file)

# t2 = time.time()

# print(t1-t2)

# print(df1)

# test_dict = {'a':'b','c':'d'}

# # with open("pickletest.pickle",'wb') as test_pickle:
# #     pickle.dump(test_dict,test_pickle)

# with open("pickletest.pickle",'rb') as recover_pickle:
#     td2 = pickle.load(recover_pickle)

# print(td2)

# pd.DataFrame.plot.hist()


arr = np.array([[1,2,3],[2,8,7]])

arr = np.where(arr == np.array([1,2,3]),np.array([9,9,9]),arr)

print(arr)

numbers = [x for x in np.arange(-1.0,1.0,0.05)]

print(numbers)


new_validation_data = {"1":{"checkpoint":"\/home\/kaue\/data\/epochs\/3321\/model.ckpt","image":"0158","accuracy":0.6587219238,"precision":0.6557100149,"recall":0.3977134672,"f1":0.4951184551,"iou":0.3290082576},"2":{"checkpoint":"\/home\/kaue\/data\/epochs\/3321\/model.ckpt","image":"0356","accuracy":0.6311721802,"precision":0.6349700551,"recall":0.2902953816,"f1":0.3984345835,"iou":0.2487782137},"3":{"checkpoint":"\/home\/kaue\/data\/epochs\/3321\/model.ckpt","image":"0743","accuracy":0.7346992493,"precision":0.6843719743,"recall":0.6857059965,"f1":0.685038336,"iou":0.5209568877},"4":{"checkpoint":"\/home\/kaue\/data\/epochs\/3321\/model.ckpt","image":"0823","accuracy":0.6654891968,"precision":0.6457001444,"recall":0.4541877459,"f1":0.5332708828,"iou":0.3635783026},"5":{"checkpoint":"\/home\/kaue\/data\/epochs\/3321\/model.ckpt","image":"1830","accuracy":0.5753822327,"precision":0.4885248873,"recall":0.1954976518,"f1":0.2792465536,"iou":0.16228156},"6":{"checkpoint":"\/home\/kaue\/data\/epochs\/3321\/model.ckpt","image":"1981","accuracy":0.6455383301,"precision":0.7378723171,"recall":0.244365265,"f1":0.3671420593,"iou":0.2248462957},"7":{"checkpoint":"\/home\/kaue\/data\/epochs\/3321\/model.ckpt","image":"2454","accuracy":0.5764389038,"precision":0.4906868452,"recall":0.1757874123,"f1":0.2588444183,"iou":0.1486624292},"8":{"checkpoint":"\/home\/kaue\/data\/epochs\/3321\/model.ckpt","image":"2545","accuracy":0.6313896179,"precision":0.6575168822,"recall":0.2586538287,"f1":0.3712610696,"iou":0.2279438789},"9":{"checkpoint":"\/home\/kaue\/data\/epochs\/3321\/model.ckpt","image":"3153","accuracy":0.7120742798,"precision":0.6537143967,"recall":0.6712814376,"f1":0.6623814636,"iou":0.4951945907},"10":{"checkpoint":"\/home\/kaue\/data\/epochs\/3321\/model.ckpt","image":"3499","accuracy":0.9283332825,"precision":0.9242866813,"recall":0.9036972565,"f1":0.9138760148,"iou":0.8414103982}}


for key in new_validation_data:
    del new_validation_data[key]["checkpoint"]
    del new_validation_data[key]["image"]



print(new_validation_data)



new_valid = pd.DataFrame(new_validation_data)

print(new_valid.T)