import cv2
import random as rnd

def showImg(image,winname="test"+str(rnd.randint(0,9999)),timeToWait=0,showSequence=False):
    cv2.namedWindow(winname,0)
    cv2.imshow(winname,image)
    if not showSequence:
        cv2.waitKey(timeToWait)
        cv2.destroyWindow(winname)