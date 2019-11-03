from processing_functions import misc as msc
from processing_functions import general_funcs as gf
import os

in_out_list = [("/home/kaue/Dropbox/data/gt/versions/only_trees","/home/kaue/Dropbox/data/gt_downsized/only_trees"),("/home/kaue/Dropbox/data/gt/versions/with_terrain_veg","/home/kaue/Dropbox/data/gt_downsized/with_terrain_veg")]

for inoutpair in in_out_list:
    try:
        os.makedirs(inoutpair[1])
    except:
        pass

    imgList = msc.orderedFileList(inoutpair[0],'*.png')
    
    for imgpath in imgList:
        imgname = msc.filenameFromPath(imgpath)
        outpath = os.path.join(inoutpair[1],imgname)
        # print(outpath)
        gf.resize_and_save(imgpath,outpath)




