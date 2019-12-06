from processing_functions import color_stuff as cs
from processing_functions import misc as msc 
from processing_functions import general_funcs as gf
import os
import cv2



classifiedImgPath = msc.joinToHome("snav/samples/0059_gt.png")
originalImgPath   = msc.joinToHome("snav/samples/0059.png")
outPath =       msc.joinToHome("snav/samples/0059_only_veg.png")

classifiedImg = cv2.imread(classifiedImgPath)
originalImg   = cv2.imread(originalImgPath)


for i,column in enumerate(classifiedImg):
    for j,pixel in enumerate(column):
        # as there are only black or white pixels, we can test only a channel
        # print(originalImg[i,j,0])
        if pixel[0] == 255:
            try:
                pixel.itemset(0,originalImg[i,j,0])
                pixel.itemset(1,originalImg[i,j,1])
                pixel.itemset(2,originalImg[i,j,2])
            except:
                print(classifiedImg.shape)


print(type(classifiedImg))

cv2.imwrite(outPath,classifiedImg)


# misc.telegram_bot_sendtext("processing ended")