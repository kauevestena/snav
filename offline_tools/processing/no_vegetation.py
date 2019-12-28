from processing_functions import misc as msc
from processing_functions import color_stuff as cs
import os

path = "/home/kaue/data/politecnico2/noveg"
destpath = "/home/kaue/data/politecnico2/all_black_masks"

filelist = msc.orderedFileList(path)

for filepath in filelist:
    filename = msc.fileNumberFromPathAsStr(filepath)+'.png'
    print(filename)
    cs.allBlackImg(filepath,os.path.join(destpath,filename))
