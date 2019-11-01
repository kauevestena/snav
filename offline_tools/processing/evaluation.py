import os
from processing_functions import validation as vd
from processing_functions import misc as msc


# OPJ = os.path.join
# OE = os.environ

# paths that contain subfolders with checkpoints
pathsWithCheckpoints = [
    msc.joinToHome("/Dropbox/data/checkpoints/deeplab_plus"),
    "/media/kauevestena/data/Semantic-Segmentation-Suite/checkpoints",
    ]
listsOfCkptFolders = []
for ckptPath in pathsWithCheckpoints:
    # print(ckptPath)
    listsOfCkptFolders.append(msc.getSubdirs(ckptPath))
# print(listsOfCkptFolders)
# removing invalid folders:
validCkptFolders = []

for listOfCkpt in listsOfCkptFolders:
    for ckptFolder in listOfCkpt:
        if(vd.check_ckpt_folder(ckptFolder)): #the filtering function
            validCkptFolders.append(ckptFolder)
        # else:
        #     print(ckptFolder)
# print(validCkptFolders)

# Ground Truth Images
gtImages = msc.joinToHome("/Dropbox/data/gt/originals")
gtImagesList = msc.orderedFileList(gtImages,'*.png')
# print(gtImagesList)

# Ground Truth Masks (gtm)
gtMasksVersions = msc.joinToHome("/Dropbox/data/gt/versions")
gtmDirs = msc.getSubdirs(gtMasksVersions)
listOfListsOnDirs = []
for dirPath in gtmDirs:
    listOfListsOnDirs.append(msc.orderedFileList(dirPath,'*.png'))


# the list of checkpoints:
ckptList = []
for validckptpath in validCkptFolders:
    ckptList.append(vd.checkpoint(validckptpath))

for ckpt in ckptList:
    print(ckpt.model,ckpt.dataset)