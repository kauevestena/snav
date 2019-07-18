from processing_functions import misc as msc
from processing_functions import color_stuff as cs

path = "/home/kaue/data/extracted_images/samples/2019-07-11-16-21-46/outliers_or_challenging/no_vegetation"

filelist = msc.orderedFileList(path)

for filepath in filelist:
    cs.allBlackImg(filepath,filepath)
