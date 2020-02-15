import os 
from processing_functions import misc as msc
from processing_functions import color_stuff as cs
from processing_functions import general_funcs as gf
import glob
import cv2

basedir = "/home/kauevestena/Dropbox/data/backup/temp/"
baseOutDir = "/home/kauevestena/Dropbox/data/gt/originals_complete_red/"

dirList = msc.getSubdirs(basedir)

subpaths = msc.subpathList(dirList,basedir)

msc.createDirStructure(baseOutDir,subpaths)


for folder in dirList:
    if msc.checkForImages(folder,'*.png'):
        print(folder)
        subpath = msc.removeBasedir(folder,basedir)
        outFolderPath = os.path.join(baseOutDir,subpath)
    
        for filepath in glob.glob(folder+"/*.png"):
            fileName = msc.filenameFromPath(filepath)
            outPath = os.path.join(outFolderPath,fileName)

            cs.save_one_band(filepath,outPath)


msc.telegram_bot_sendtext("band extraction terminated")

