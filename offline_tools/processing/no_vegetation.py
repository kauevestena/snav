from processing_functions import misc as msc
from processing_functions import color_stuff as cs
import os

path = "/home/kaue/data/politecnico_v2/val"
destpath = "/home/kaue/data/politecnico_v2/downsized"

filelist = msc.orderedFileList(path)

for filepath in filelist:
    filename = msc.fileNumberFromPathAsStr(filepath)+'.png'
    print(filename)
    cs.allBlackImg(filepath,os.path.join(destpath,filename),(512,512))
