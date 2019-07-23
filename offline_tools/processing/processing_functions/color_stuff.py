import cv2
import numpy as np

# def compare_quickly(pixel,vR,vG,vB):
#     equal = False

#     if pixel[0] == vB:
#         if pixel

# return equal

def save_one_band(imPath,outPath,channel=2):
    """
        to save only one band, generally the red band
    """
    splitted = []
    img = cv2.imread(imPath)
    splitted = cv2.split(img)
    cv2.imwrite(outPath,splitted[channel])

def remove_other_classes(imPath,outPath,classR,classG,classB):
    """
    mantains only the specified class
    """
    img = cv2.imread(imPath)
    classColor = np.array([classB,classG,classR])
    for column in img:
        for pixel in column:
            if not np.array_equal(pixel,classColor):
                pixel.itemset(0,0)
                pixel.itemset(1,0)
                pixel.itemset(2,0)

    cv2.imwrite(outPath,img)

def trueInBoolList(inputList):
    thereIs = False

    for item in inputList:
        if item:
            # print("pass")
            thereIs = True
            break

    return thereIs

def remove_other_classes2(imPath,outPath,listOfClasses):
    # print(listOfClasses)
    """
    mantains only the specified class, you can input a list of classes, must be a list of np_array
    """
    # TODO: check the input list
     
    img = cv2.imread(imPath)
    for column in img:
        for pixel in column:
            test = []
            for label in listOfClasses:
                # print(pixel,label)
                test.append(np.array_equal(pixel,label))

            # print(test)
            if trueInBoolList(test):
                pixel.itemset(0,255)
                pixel.itemset(1,255)
                pixel.itemset(2,255)
            else:
                # print(pixel)
                pixel.itemset(0,0)
                pixel.itemset(1,0)
                pixel.itemset(2,0)

    cv2.imwrite(outPath,img)

def allBlackImg(imPath,outPath):
    img = cv2.imread(imPath)
    for column in img:
        for pixel in column:
            pixel.itemset(0,0)
            pixel.itemset(1,0)
            pixel.itemset(2,0)

    cv2.imwrite(outPath,img)

def setPixelVal(pixel,vR,vG,vB):
        pixel.itemset(0,vB)
        pixel.itemset(1,vG)
        pixel.itemset(2,vR)
        return pixel

def setAllPixelVals(imPath,vR,vG,vB):
    img = cv2.imread(imPath)
    for column in img:
        for pixel in column:
            setPixelVal(pixel,vR,vG,vB)

    cv2.imwrite(outPath,img)

def checkIfPixVal(imPath,vR=255,vG=255,vB=255):
    img = cv2.imread(imPath)

    exist = False

    for column in img:
        if (exist):
            break
        for pixel in column:
            if np.array_equal(pixel,np.array([vB,vG,vR])):
                exist = True
                break

    return exist

def chg_specific_pix_val(imPath,outPath,vR=255,vG=255,vB=255,nvR=254,nvG=254,nvB=254):
    img = cv2.imread(imPath)

    for column in img:
        for pixel in column:
            if np.array_equal(pixel,np.array([vB,vG,vR])):
                setPixelVal(pixel,nvB,nvG,nvR)

    cv2.imwrite(outPath,img)