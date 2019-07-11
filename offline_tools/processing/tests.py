import numpy as np
import cv2
from processing_functions import general_funcs as gf
from processing_functions import color_stuff as cs


imsample = "/home/kauevestena/tests/CamVid/test_labels/0006R0_f03720_L.png"

# img = cv2.imread(imsample)

# for column in img:
#     for pixel in column:
#         # pixel.itemset(0,200)
#         # pixel.itemset(1,20)
#         # pixel.itemset(2,20)
#         print(pixel-np.array([1,1,1]))

cs.remove_other_classes(imsample,"test.png",128,128,0)
