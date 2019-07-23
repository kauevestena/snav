import numpy as np
import cv2
from processing_functions import general_funcs as gf
from processing_functions import color_stuff as cs
from processing_functions import misc as msc

# test = [[293,3,0],[234,22]]

# print(msc.listOfLists_npArrays(test))


imPath = "/home/kauevestena/tests/CamVid/test_labels/0006R0_f01380_L.png"

labels = [[0,128,128],[0,192,192]]
labels = msc.listOfLists_npArrays(labels)

cs.remove_other_classes2(imPath,"test.png",labels)

