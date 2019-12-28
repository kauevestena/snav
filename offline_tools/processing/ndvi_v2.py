from processing_functions import color_stuff as cs
from processing_functions import misc as msc 
from processing_functions import general_funcs as gf
import os
import cv2
import numpy as np
import time

outfolder = msc.joinToHome("data/cnn_output/ndvi_v2")

input_path = msc.joinToHome("data/cnn_output/only_veg")


stats_path = msc.joinToHome("data/cnn_output/ndvi_stats.csv")
if os.path.exists(stats_path):
    os.remove(stats_path)



img_inputlist = msc.orderedFileList(input_path,'*.png')


for i,imgpath in enumerate(img_inputlist):
    t1 = time.time()



    imgname = msc.filenameFromPathWtithoutExt(imgpath)

    outpath = os.path.join(outfolder,imgname+'.png')

    print(outpath)

    cs.gen_uint8_NDVI(imgpath,outpath,absolute_scale=True,print_stats=True)

    msc.print_rem_time_info(len(img_inputlist),i,t1)
