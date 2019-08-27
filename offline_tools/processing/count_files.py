from processing_functions import misc as msc

basepath = "/media/kauevestena/data/Semantic-Segmentation-Suite/Cityscapes"

ext = '*.png'

folderlist = msc.getSubdirs(basepath)

for folder in folderlist:
    if msc.checkForImages(folder,ext):
        filelist = msc.orderedFileList(folder,ext)
        print(folder)
        print(len(filelist))