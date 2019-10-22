#script to classify vegetation and no vegatation in a manualy classified in white for vegetation and anything to non-vegetation
from processing_functions import misc as msc 
from processing_functions import color_stuff as cs
import datetime
import os
# import cv2

# inputpath = "/home/kaue/data/extracted_images/samples/2019-07-11-16-21-46/regular"
inputpath = "/home/kaue/data/extracted_images/samples/2019-07-11-16-21-46/reclassification"

# outpath = "/home/kaue/data/extracted_images/samples/2019-07-11-16-21-46/already_classified"
outpath = "/home/kaue/data/extracted_images/samples/2019-07-11-16-21-46/reclassification_blackwhite"


imagelist = msc.orderedFileList(inputpath,extension='*.png')

minDate = datetime.datetime(year=2019,day=17,month=7)

for imgpath in imagelist:
    filedate = msc.getModTime(imgpath)
    if filedate > minDate:
        savepath = os.path.join(outpath,msc.filenameFromPath(imgpath)) 
        # cs.remove_other_classes(imgpath,savepath,255,255,255)
        cs.remove_other_classes(imgpath,savepath,0,0,0,255,255,255)
        print(imgpath)


msc.telegram_bot_sendtext("GT classification ended")

