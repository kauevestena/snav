import cv2
import numpy as np

def save_one_band(imPath,outPath,channel=2):
    """
        to save only one band, generally the red band
    """
    splitted = []
    img = cv2.imread(imPath)
    splitted = cv2.split(img)
    cv2.imwrite(outPath,splitted[channel])

def remove_other_classes(imPath,outPath,classR,classG,classB):
    img = cv2.imread(imPath)
    classColor = np.array([classB,classG,classR])
    for column in img:
        for pixel in column:
            if not np.array_equal(pixel,classColor):
                pixel.itemset(0,0)
                pixel.itemset(1,0)
                pixel.itemset(2,0)

    cv2.imwrite(outPath,img)