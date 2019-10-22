from processing_functions import color_stuff as cs
from processing_functions import misc
from processing_functions import general_funcs as gf
import os
import cv2

"""
    initially i've trated grass and soil vegtation as "vegetation", but now i will only use not grass vegetation
"""


classifiedPath = "/home/kaue/data/extracted_images/gt/only_trees"
toClassifyFolder = "/home/kaue/data/extracted_images/gt/originals"

originalsPath = "/home/kaue/data/extracted_images/2019-07-11-16-21-46/ngr"

classifiedList = misc.orderedFileList(classifiedPath,'*.png')

for path in classifiedList:
    # print(path)
    filename = misc.filenameFromPath(path)
    # print(filename)
    originalImgPath = os.path.join(originalsPath,misc.modFilenameExt(filename,'.jpg'))
    outPath  = os.path.join(toClassifyFolder,misc.fileNumberFromPathAsStr(filename)+'.png')

    print(originalImgPath,outPath, filename)

    # classifiedImg = cv2.imread(path)
    originalImg   = cv2.imread(originalImgPath)

    # for i,column in enumerate(classifiedImg):
    #     for j,pixel in enumerate(column):
    #         # as there are only black or white pixels, we can test only a channel
    #         # print(originalImg[i,j,0])
    #         if pixel[0] == 255:
    #             try:
    #                 pixel.itemset(0,originalImg[i,j,0])
    #                 pixel.itemset(1,originalImg[i,j,1])
    #                 pixel.itemset(2,originalImg[i,j,2])
    #             except:
    #                 print(classifiedImg.shape)

    cv2.imwrite(outPath,originalImg)


misc.telegram_bot_sendtext("processing ended")