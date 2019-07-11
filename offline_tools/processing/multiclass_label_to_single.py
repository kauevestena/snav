import cv2
import glob
from processing_functions import color_stuff as cs


folderlist =[
    "/home/kauevestena/tests/CamVid/test_labels",
    "/home/kauevestena/tests/CamVid/train_labels",
    "/home/kauevestena/tests/CamVid/val_labels"
]

treeR = 128
treeG = 128
treeB = 0

for folder in folderlist:
    print(folder)
    # for filepath in glob.glob(os.path.join(folder,"*.png'")):
    # joinedpath = os.path.join(folder,"")
    for filepath in glob.glob(folder+"/*.png"):
        cs.remove_other_classes(filepath,filepath,treeR,treeG,treeB)
