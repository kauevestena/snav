import os
import sys
from processing_functions import misc as msc

defaultPath =  "/home/kaue/data/extracted_images/samples/2019-07-11-16-21-46/regular"

if len(sys.argv) < 2:
    # print("insert pathname")
    # sys.exit()
    path = defaultPath
else:
    path = sys.argv[1]

filePathList = msc.orderedFileList(path,'*.png',1)

basePath = msc.pathWithoutFilename(sys.argv[0])

#create file to store the last opened image:
lastOpenedPath = os.path.join(basePath,'last_opened.txt')

if not os.path.exists(lastOpenedPath):
    # storageFile = open(lastOpenedPath,'w')
    # storageFile.close()
    msc.writeToFile(lastOpenedPath,"")

if os.stat(lastOpenedPath).st_size == 0:
    # storageFile = open(lastOpenedPath,'w')
    # storageFile.write("-1")
    # storageFile.close()]
    msc.writeToFile(lastOpenedPath,"-1")


for filePath in filePathList:

    fileNumber = msc.fileNumberFromPath(filePath)
    # print(msc.readNumberFromFile(lastOpenedPath))
    if msc.readNumberFromFile(lastOpenedPath) < fileNumber: 
        os.system("kolourpaint "+filePath)
        # os.system("gimp "+filePath)
        msc.writeToFile(lastOpenedPath,str(fileNumber))

