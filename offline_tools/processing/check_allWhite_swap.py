import os 
from processing_functions import misc as msc
from processing_functions import color_stuff as cs
import glob

basedir = "/home/kaue/data/extracted_images/samples/2019-07-11-16-21-46"

onlyCheck = False

dirList = msc.getSubdirs(basedir)

for folder in dirList:
    if msc.checkForImages(folder,'*.png'):
        imList = msc.orderedFileList(folder,'*.png',True)
        for filePath in imList:
            print(filePath)
            if cs.checkIfPixVal(filePath):
                if onlyCheck:
                    print(filePath)
                else:
                    cs.chg_specific_pix_val(filePath,filePath)