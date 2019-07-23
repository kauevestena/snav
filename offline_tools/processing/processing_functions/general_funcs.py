import cv2
import os
import random as rnd

def showImg(image,winname="test"+str(rnd.randint(0,9999)),timeToWait=0,showSequence=False):
    cv2.namedWindow(winname,0)
    cv2.imshow(winname,image)
    if not showSequence:
        cv2.waitKey(timeToWait)
        cv2.destroyWindow(winname)

def saveJPG_as_PNG(imPath,delete=False):
    img = cv2.imread(imPath)
    path2 = os.path.splitext(imPath)[0]
    # print(path2)
    cv2.imwrite(path2+'.png',img)
    if delete:
        os.remove(imPath)
     