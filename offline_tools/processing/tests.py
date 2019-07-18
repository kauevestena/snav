import numpy as np
import cv2
from processing_functions import general_funcs as gf
from processing_functions import color_stuff as cs


imsample = "/home/kaue/tests/imgs/3806.png"

# img = cv2.imread(imsample)

# for column in img:
#     for pixel in column:
#         # pixel.itemset(0,200)
#         # pixel.itemset(1,20)
#         # pixel.itemset(2,20)
#         print(pixel-np.array([1,1,1]))

cs.chg_specific_pix_val(imsample,imsample,255,255,255,255,0,0)
