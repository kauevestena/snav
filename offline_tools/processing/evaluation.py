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
    try:
        listsOfCkptFolders.append(msc.getSubdirs(ckptPath))
    except:
        print("path "+ckptPath+" not avaliable")
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
gtMasksVersions = msc.joinToHome("/Dropbox/data/gt_downsized")
gtmDirs = msc.getSubdirs(gtMasksVersions)
listOfListsOnDirs = []
for dirPath in gtmDirs:
    listOfListsOnDirs.append(msc.orderedFileList(dirPath,'*.png'))

# list of images and ground truth versions
imgs_and_gts = []

for i,imagepath in enumerate(gtImagesList):

    img_gts = vd.img_and_gts(imagepath)

    for a_list in listOfListsOnDirs:
        img_gts.add_entry(a_list[i])

    # img_gts.print_state()

    imgs_and_gts.append(img_gts)


# the list of checkpoints:
ckptList = []
for validckptpath in validCkptFolders:
    ckptList.append(vd.checkpoint(validckptpath))

# for ckpt in ckptList:
#     print(ckpt.model,ckpt.dataset)


# print(listOfListsOnDirs[0][0])

# ckptList[0].process_image(gtImagesList[0])
ckptList[0].process_and_validate(imgs_and_gts[0])