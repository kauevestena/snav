from processing_functions import misc as msc
from os.path import join
from os import listdir, rmdir
from shutil import move
import os
# import numpy as np

basedir = "/media/kauevestena/data/gtFine_trainvaltest/gtFine"

strToReplace = "_gtFine_color"

strToAdd = '_L'

strToContain = 'color'

pathlist = msc.getSubdirs(basedir)

# sizes = np.empty(len(pathlist), dtype=int)

# print(sizes)

# for i,path in enumerate(pathlist):
#     sizes[i] = path.count('/')

# print(sizes)

# max_lvl = np.max(sizes)

# print(max_lvl)

for path in pathlist:
    if msc.checkForImages(path,'*.png'):
        parent = msc.get_parent_dir(path)S
        imgList = msc.orderedFileList(path,'*.png')
        for imgPath in imgList:
            if strToContain in imgPath:
                filename = msc.filenameFromPath(imgPath)
                newfilename = filename.replace(strToReplace,strToAdd)
                print(newfilename)
                move(imgPath,os.path.join(parent,newfilename))
        # os.removedirs(path)


msc.telegram_bot_sendtext("copying terminated")