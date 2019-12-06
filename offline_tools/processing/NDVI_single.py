from processing_functions import color_stuff as cs
from processing_functions import misc as msc 
from processing_functions import general_funcs as gf
import os
import cv2
import numpy as np



print(np.__version__)

inputimgpath =       msc.joinToHome("snav/samples/0059_only_veg.png")

outpath = msc.joinToHome("snav/samples/0059_only_veg_ndvi.png")

# inputimg = cv2.imread(inputimgpath)

cs.gen_uint8_NDVI(inputimgpath,outpath,True,True)



# misc.telegram_bot_sendtext("processing ended")