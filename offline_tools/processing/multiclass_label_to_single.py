import cv2
import glob
from processing_functions import color_stuff as cs
from processing_functions import misc as msc


folderlist =[
    "/home/kauevestena/tests/CamVid/test_labels",
    "/home/kauevestena/tests/CamVid/train_labels",
    "/home/kauevestena/tests/CamVid/val_labels"
]

treeR = 128
treeG = 128
treeB = 0

# BGR order
labels = [[0,128,128],[0,192,192]]
labels = msc.listOfLists_npArrays(labels)

for folder in folderlist:
    print(folder)
    # for filepath in glob.glob(os.path.join(folder,"*.png'")):
    # joinedpath = os.path.join(folder,"")
    for filepath in glob.glob(folder+"/*.png"):
        print(filepath)
        cs.remove_other_classes2(filepath,filepath,labels)
