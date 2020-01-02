import os, time
from processing_functions import validation as vd
from processing_functions import misc as msc
import copy


# OPJ = os.path.join
# OE = os.environ

# paths that contain subfolders with checkpoints
pathsWithCheckpoints = [
    # IN THE SEARCH FOR REAL METRICS
    "/home/kaue/data/epochs"

    # # CHECKPOINTS FROM CITYSCAPES TRAINED CNNS
    # msc.joinToHome("/Dropbox/data/checkpoints/deeplab_plus"),
    # "/media/kauevestena/data/Semantic-Segmentation-Suite/checkpoints",
    # "/home/kaue/Downloads/parts/checkpoints",
    # "/media/kauevestena/data/Semantic-Segmentation-Suite/checkpoints"
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

print(gtmDirs)


listOfListsOnDirs = []
for dirPath in gtmDirs:
    listOfListsOnDirs.append(msc.orderedFileList(dirPath,'*.png'))



# list of images and ground truth versions
imgs_and_gts = []

for i,imagepath in enumerate(gtImagesList):
    # print(i,imagepath)

    img_gts = vd.img_and_gts(imagepath)

    for a_list in listOfListsOnDirs:
        # print(msc.pathWithoutFilename(a_list[i]))
        print(a_list[i])
        img_gts.add_entry(a_list[i])

    # img_gts.print_state()

    # THIS WORKAROUND IS SO STRANGE:

    img_gts.versions_dicts = img_gts.versions_dicts

    imgs_and_gts.append(copy.deepcopy(img_gts))
    # imgs_and_gts.append(img_gts)


    # img_gts.reset_dict()


# for item in imgs_and_gts:
#     print(item.versions_dicts)

print([item.versions_dicts for item in imgs_and_gts])

# the list of checkpoints:
ckptList = []
for validckptpath in validCkptFolders:
    if os.environ['HOME'] == '/home/kauevestena':
        ckptList.append(vd.checkpoint(validckptpath,"python3.7"))
    else:
        ckptList.append(vd.checkpoint(validckptpath))

# for ckpt in ckptList:
#     print(ckpt.model,ckpt.dataset)


# print(listOfListsOnDirs[0][0])

# ckptList[0].process_image(gtImagesList[0])
# ckptList[0].process_and_validate(imgs_and_gts[0])
# ckptList[0].process_and_validate(imgs_and_gts[1])



# print(ckptList[0].error_metrics_store)

# ckptList[0].dump_to_tinyDB()

print(len(ckptList),len(imgs_and_gts))

total_its = len(ckptList) * len(imgs_and_gts)

for i,ckpt in enumerate(ckptList):
    for j,img in enumerate(imgs_and_gts):
        beg = time.time()
        ckpt.process_and_validate(img,True,False)
        msc.print_rem_time_info(total_its,i*len(imgs_and_gts)+j,beg)
    ckpt.dump_to_tinyDB()


msc.telegram_bot_sendtext("evaluation done")