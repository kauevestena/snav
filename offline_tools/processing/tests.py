import numpy as np
import cv2
from processing_functions import general_funcs as gf
from processing_functions import color_stuff as cs
from processing_functions import misc as msc
import requests
import os

import requests

imgpath = "/home/kaue/data/cityscapes_red/test/berlin/berlin_000000_000019_leftImg8bit.png"
imgpath2 = "/home/kaue/data/cityscapes_original/leftImg8bit/test/berlin/berlin_000000_000019_leftImg8bit.png"

img = cv2.imread(imgpath)

# cv2.imshow(imgpath,img)
# cv2.waitKey(0)

# print(msc.fileNumberFromPathAsStr('test.png'))

print(img.shape)
