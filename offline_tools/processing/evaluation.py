import os
from processing_functions import misc as msc


OPJ = os.path.join
OE = os.environ

# paths that contain subfolders with checkpoints
pathsWithCheckpoints = [
    msc.joinToHome("/data/checkpoints/deeplab_plus"),
    "/media/kauevestena/data/Semantic-Segmentation-Suite/checkpoints",
    ]

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
