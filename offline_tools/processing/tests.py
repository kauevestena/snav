
import pandas as pd
import pickle
# import cPiclke
import numpy as np
# from tinydb import TinyDB, Query, where
# from processing_functions import misc as msc
import time
from processing_functions import misc as msc


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


new_validation_data = {"1":{"checkpoint":"\/home\/kaue\/data\/epochs\/3321\/model.ckpt","image":"0158","accuracy":0.94008255,"precision":0.8308669656,"recall":0.9267719292,"f1":0.8762029367,"iou":0.7796807496},"2":{"checkpoint":"\/home\/kaue\/data\/epochs\/3321\/model.ckpt","image":"0356","accuracy":0.9628143311,"precision":0.8458136676,"recall":0.9557861241,"f1":0.8974434508,"iou":0.8139659154},"3":{"checkpoint":"\/home\/kaue\/data\/epochs\/3321\/model.ckpt","image":"0743","accuracy":0.957988739,"precision":0.9508383629,"recall":0.9495752756,"f1":0.9502063995,"iou":0.9051363993},"4":{"checkpoint":"\/home\/kaue\/data\/epochs\/3321\/model.ckpt","image":"0823","accuracy":0.9311637878,"precision":0.8036579707,"recall":0.9568466768,"f1":0.873587536,"iou":0.7755485348},"5":{"checkpoint":"\/home\/kaue\/data\/epochs\/3321\/model.ckpt","image":"1830","accuracy":0.9694442749,"precision":0.8449896917,"recall":0.9696347329,"f1":0.9030313302,"iou":0.8232061271},"6":{"checkpoint":"\/home\/kaue\/data\/epochs\/3321\/model.ckpt","image":"1981","accuracy":0.9909744263,"precision":0.9562253614,"recall":0.9785129987,"f1":0.9672408064,"iou":0.9365598606},"7":{"checkpoint":"\/home\/kaue\/data\/epochs\/3321\/model.ckpt","image":"2454","accuracy":0.9606704712,"precision":0.7612491775,"recall":0.9717017703,"f1":0.8536966085,"iou":0.7447387967},"8":{"checkpoint":"\/home\/kaue\/data\/epochs\/3321\/model.ckpt","image":"2545","accuracy":0.9404525757,"precision":0.6563875637,"recall":0.9759775196,"f1":0.7848973405,"iou":0.6459514629},"9":{"checkpoint":"\/home\/kaue\/data\/epochs\/3321\/model.ckpt","image":"3153","accuracy":0.9113388062,"precision":0.9342497925,"recall":0.870117589,"f1":0.9010439729,"iou":0.8199090324},"10":{"checkpoint":"\/home\/kaue\/data\/epochs\/3321\/model.ckpt","image":"3499","accuracy":0.9283332825,"precision":0.9242866813,"recall":0.9036972565,"f1":0.9138760148,"iou":0.8414103982}}


# for key in new_validation_data:
#     del new_validation_data[key]["checkpoint"]
#     del new_validation_data[key]["image"]



# print(new_validation_data)



# new_valid = pd.DataFrame(new_validation_data)*100

# print(new_valid.T)
# print(new_valid.T.mean())
# print(new_valid.T.std())
# print(new_valid.T.median())
# print(new_valid.T.min())
# print(new_valid.T.max().to_dict())




p1 =  
p2 =  "/media/kauevestena/data/Semantic-Segmentation-Suite/checkpoints"


print(msc.getSubdirs(p1))
print(msc.getSubdirs(p2))
