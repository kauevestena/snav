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


t1 = {'with_terrain_veg': [{'accuracy': 0.6908493041992188, 'precision': 0.6503000433052193, 'recall': 0.5723438237322589, 'f1': 0.608836675000724, 'iou': 0.437645719995559}, {'accuracy': 0.5722846984863281, 'precision': 0.4706205214209483, 'recall': 0.14005953029148063, 'f1': 0.2158737263184396, 'iou': 0.12099688766590622}], 'only_trees': [{'accuracy': 0.7885513305664062, 'precision': 0.709030169302786, 'recall': 0.7164916229057264, 'f1': 0.7127413687669074, 'iou': 0.5536893297690747}, {'accuracy': 0.6472663879394531, 'precision': 0.5534990089952737, 'recall': 0.18913061598733016, 'f1': 0.28192683135177954, 'iou': 0.16409477576184922}]}

print(t1)

df = pd.DataFrame(t1['with_terrain_veg'])

print(df.T)