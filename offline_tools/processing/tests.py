
import pandas as pd
import numpy as np
from tinydb import TinyDB, Query, where
from processing_functions import misc as msc


t1 = {'with_terrain_veg': [{'checkpoint': '/home/kauevestena/Dropbox/data/checkpoints/deeplab_plus/0012/model.ckpt', 'image': '0359', 'accuracy': 0.7071266174316406, 'precision': 0.8746151429469055, 'recall': 0.2766663685240949, 'f1': 0.4203604297373408, 'iou': 0.26611161030072455}, {'checkpoint': '/home/kauevestena/Dropbox/data/checkpoints/deeplab_plus/0012/model.ckpt', 'image': '0437', 'accuracy': 0.612396240234375, 'precision': 0.48549038093274016, 'recall': 0.1637697146775588, 'f1': 0.24492070805404037, 'iou': 0.13954965406861042}], 'only_trees': [{'checkpoint': '/home/kauevestena/Dropbox/data/checkpoints/deeplab_plus/0012/model.ckpt', 'image': '0359', 'accuracy': 0.7330970764160156, 'precision': 0.8462142632736412, 'recall': 0.29274946471464125, 'f1': 0.4350073079935722, 'iou': 0.2779612391901096}, {'checkpoint': '/home/kauevestena/Dropbox/data/checkpoints/deeplab_plus/0012/model.ckpt', 'image': '0437', 'accuracy': 0.638092041015625, 'precision': 0.4577968947942138, 'recall': 0.16888932363841883, 'f1': 0.24674870980547836, 'iou': 0.14073778880727464}]}




db = TinyDB(msc.joinToHome("Dropbox/data/tinydbs/validation/only_trees.json"))

# print(db.all())

imgname  = '0059'
ckptname = '/home/kaue/Dropbox/data/checkpoints/deeplab_plus/0036/model.ckpt'

for entry in db:
    print(entry)

print("{:.4f} test".format(1.3895432964532942378423786))