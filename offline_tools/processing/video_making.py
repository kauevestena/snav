import os,time
from processing_functions import misc as msc
from processing_functions import color_stuff as cs
import cv2
import numpy as np
from cv2 import VideoWriter, VideoWriter_fourcc

out_basepath = msc.joinToHome("/data/cnn_output3")
out_dirs = ['orig_resiz','overlay','masks','ndvi','only_veg']

outpaths = {}

### VIDEO CONFIGURATION

videopath = msc.joinToHome("/data/CNN_VIDEO/smmt_video2.avi")


width = 1024
height = 1024
FPS = 15
seconds = 127

fourcc = VideoWriter_fourcc(*'MP42')
video = VideoWriter(videopath, fourcc, float(FPS), (width, height))

############3

for name in out_dirs:
    outpaths[name] = os.path.join(out_basepath,name)

imgs_path = "/home/kaue/data/extracted_images/2019-07-11-16-21-46/ngr"

img_list = msc.orderedFileList(imgs_path)

for i,img_path in enumerate(img_list):
    t1 = time.time()

    img_name = msc.fileNumberFromPathAsStr(img_path)

    dest_orig = os.path.join(outpaths['orig_resiz'],img_name+'.png')
    dest_pred = os.path.join(outpaths['masks'],img_name+'.png')

    dest_onlyveg = os.path.join(outpaths['only_veg'],img_name+'.png')

    dest_ndvi = os.path.join(outpaths['ndvi'],img_name+'.png')
    dest_overlay = os.path.join(outpaths['overlay'],img_name+'.png')

    # allpaths = [dest_ndvi,dest_onlyveg,dest_orig,dest_overlay,dest_pred]

    # print('\n'.join(allpaths),'\n\n')
    # msc.print_rem_time_info(len(img_list),i,t1)
    # print(i)

    orig = cv2.imread(dest_orig)
    pred = cv2.imread(dest_pred)
    onlyveg = cv2.imread(dest_onlyveg)
    ndvi = cv2.imread(dest_ndvi)
    overlay = cv2.imread(dest_overlay)

    # print(orig.shape,onlyveg.shape,ndvi.shape,overlay.shape)

    cs.labelimg(orig,"Photograph")
    cs.labelimg(onlyveg,"Only Veg.")
    cs.labelimg(pred,"Pred. Mask")
    cs.labelimg(overlay,"Overlay")

    combinedimg = cs.disp_multiple(orig,pred,onlyveg,overlay)


    # # # cv2.imshow('combined',combinedimg)
    # # # cv2.waitKey(0)

    # # # if i > 1:
    # # #     break
    
    video.write(combinedimg)

    if i == 1914:
        break


video.release()
