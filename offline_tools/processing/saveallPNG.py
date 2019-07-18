import os 
from processing_functions import misc as msc
from processing_functions import color_stuff as cs
from processing_functions import general_funcs as gf
import glob

basedir = "/home/kaue/data/extracted_images/samples/2019-07-11-16-21-46"

dirList = msc.getSubdirs(basedir)

for folder in dirList:
    if msc.checkForImages(folder):
        imList = msc.orderedFileList(folder)
        for filePath in imList:
            gf.saveJPG_as_PNG(filePath,True)