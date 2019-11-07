# # # # import numpy as np
# # # # import cv2
# # # # from processing_functions import general_funcs as gf
# # # # from processing_functions import color_stuff as cs
# # # # from processing_functions import misc as msc
# # # # import requests
# # # # import os

# # # # import requests

# # # # # imgpath = "/home/kaue/data/cityscapes_red/test/berlin/berlin_000000_000019_leftImg8bit.png"
# # # # # imgpath2 = "/home/kaue/data/cityscapes_original/leftImg8bit/test/berlin/berlin_000000_000019_leftImg8bit.png"

# # # # # img = cv2.imread(imgpath)

# # # # # # cv2.imshow(imgpath,img)
# # # # # # cv2.waitKey(0)

# # # # # # print(msc.fileNumberFromPathAsStr('test.png'))

# # # # # print(img.shape)

# # # # import screeninfo

# # # # # screeninfo.

# # # lineToUse = 'all_model_checkpoint_paths: "../latest_model_DeepLabV3_plus_cityscapes.ckpt"'


# # # if "latest_model" in lineToUse:
# # #     a = lineToUse.split("latest_model_")[1].split('.')[0].rsplit('_',maxsplit=1)
# # #     print(a)


# # # dictTest = {}

# # # import 

# # import processing_functions.misc as msc

# # teststring = "/home/kaue/Dropbox/data/gt_downsized/with_terrain_veg/3519.png"


# # print(msc.get_only_parent_dir(teststring))


# # t1 = ['a','b','c','d']

# # print(t1[1:4])


# # a = 'aab'

# # print(a.split('a'))


# error_metrics = dict.fromkeys(["accuracy", "class_accuracies", "prec", "rec", "f1", "iou"])

# i = 0 

# for key in error_metrics:
#     error_metrics[key] = i
#     i += 1


# d1 = {'a':[],'b':[1,2]}

# d1['a'].append(1.2)
# d1['b'].pop(1)

# print(d1)

import pandas as pd
import numpy as np
from tinydb import TinyDB, Query, where


t1 = {'with_terrain_veg': [{'checkpoint': '/home/kauevestena/Dropbox/data/checkpoints/deeplab_plus/0012/model.ckpt', 'image': '0359', 'accuracy': 0.7071266174316406, 'precision': 0.8746151429469055, 'recall': 0.2766663685240949, 'f1': 0.4203604297373408, 'iou': 0.26611161030072455}, {'checkpoint': '/home/kauevestena/Dropbox/data/checkpoints/deeplab_plus/0012/model.ckpt', 'image': '0437', 'accuracy': 0.612396240234375, 'precision': 0.48549038093274016, 'recall': 0.1637697146775588, 'f1': 0.24492070805404037, 'iou': 0.13954965406861042}], 'only_trees': [{'checkpoint': '/home/kauevestena/Dropbox/data/checkpoints/deeplab_plus/0012/model.ckpt', 'image': '0359', 'accuracy': 0.7330970764160156, 'precision': 0.8462142632736412, 'recall': 0.29274946471464125, 'f1': 0.4350073079935722, 'iou': 0.2779612391901096}, {'checkpoint': '/home/kauevestena/Dropbox/data/checkpoints/deeplab_plus/0012/model.ckpt', 'image': '0437', 'accuracy': 0.638092041015625, 'precision': 0.4577968947942138, 'recall': 0.16888932363841883, 'f1': 0.24674870980547836, 'iou': 0.14073778880727464}]}

# for key in t1:
#     for entry in t1[key]:
#         print(entry.values()) 

# print(t1)

# df = pd.DataFrame(t1['with_terrain_veg'])

# print(df.T)

# print(list(df['accuracy']))


# # df2 = pd.DataFrame(t1)

# # print(df2)

# test2 = [{"name":'01','rcd1':[0.1,0.2,0.4]},{"name":'02','rcd1':[0.5,0.6,0.7]},{"name":'03','rcd1':[0.85,0.9,0.875]}]

# from tinydb import TinyDB, Query

# mydb1 = TinyDB('db_test.json')
# mydb1.purge()

# for entry in test2:
#     mydb1.insert(entry)



# print(mydb1.all())
# mydb1.all()
# imgname
# imgname
# imgname
# for entry in outDict:
#     entry['rcd1'] = np.array(entry['rcd1'])

# df2 = pd.DataFrame(outDict)

# print(df2)

# # print(outDict)

# import matplotlib.pyplot as plt

# plt.close('all')


# # df2.plot()

# test_csv = "/home/kaue/snav/offline_tools/tests/test_data.csv"

# df3 = pd.read_csv(test_csv)


# plt.figure()

# print(df3)

# df3.plot()

# import os

# scrpath = os.path.dirname(os.path.abspath(__file__))


# plt.savefig(os.path.join(scrpath,'figures/test_df.png'))

# for key in t1:
#     for entry in t1[key]:
#         print(entry)


# print(t1)
# /home/kauevestena/Dropbox/data/tinydbs/validation/only_trees.json
db = TinyDB("/home/kauevestena/Dropbox/data/tinydbs/validation/only_trees.json")

# print(db.all())

imgname  = '0359'
ckptname = '/home/kauevestena/Dropbox/data/checkpoints/deeplab_plus/0012/model.ckpt'

print(db.search((Query().checkpoint == imgname) & (Query().image == ckptname)))