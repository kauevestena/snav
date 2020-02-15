import cv2
import numpy as np
import matplotlib.pyplot as plt
import processing_functions.misc as msc
import os


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

def remove_other_classes(imPath,outPath,classR,classG,classB,setR=0,setG=0,setB=0):
    """
    mantains only the specified class
    """
    img = cv2.imread(imPath)
    classColor = np.array([classB,classG,classR])
    for column in img:
        for pixel in column:
            if not np.array_equal(pixel,classColor):
                pixel.itemset(0,setB)
                pixel.itemset(1,setG)
                pixel.itemset(2,setR)

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

def allBlackImg(imPath,outPath,anotherRes=None):
    img = cv2.imread(imPath)
    # for column in img:
    #     for pixel in column:
    #         pixel.itemset(0,0)
    #         pixel.itemset(1,0)
    #         pixel.itemset(2,0)

    #TODO: check if another input is a Tuple

    # lot better:
    if anotherRes:
        img = np.zeros(anotherRes)
    else:
        img = np.zeros(img.shape)

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

# def checkPixVal(pixel,vr)

def binarize_img(input_path, color_to_be_white: tuple):
    img = cv2.imread(input_path)

    cbw = color_to_be_white

    # cv2.imshow('teste',img)
    # cv2.waitKey(0)
    # for column in img:
    #     for pixel in column:
    #         if np.array_equal(pixel,np.array(list(color_to_be_white))):
    #             pixel.itemset(0,255)
    #             pixel.itemset(1,255)
    #             pixel.itemset(2,255)
    #         else:
    #             setPixelVal(pixel,0,0,0)

    black_region = np.where((img[:,:,0] != cbw[0]) & (img[:,:,1] != cbw[1]) & (img[:,:,2] != cbw[2]))
    white_region = np.where((img[:,:,2] == cbw[0]) & (img[:,:,1] == cbw[1]) & (img[:,:,0] == cbw[2]))

    # print(white_region)

    img[white_region]=(255,255,255)
    img[black_region]=(0,0,0)


    return img

def gen_only_veg_img(classifiedImgPath,originalImgPath,outPath):
    classifiedImg = cv2.imread(classifiedImgPath)
    originalImg   = cv2.imread(originalImgPath)

    for i,column in enumerate(classifiedImg):
        for j,pixel in enumerate(column):
            # as there are only black or white pixels, we can test only a channel
            # print(originalImg[i,j,0])
            if pixel[0] == 255:
                try:
                    pixel.itemset(0,originalImg[i,j,0])
                    pixel.itemset(1,originalImg[i,j,1])
                    pixel.itemset(2,originalImg[i,j,2])
                except:
                    print(classifiedImg.shape)

    cv2.imwrite(outPath,classifiedImg)

def gen_uint8_NDVI(imgpath,outimgpath,absolute_scale = True,second_img=True,print_stats=False):
    img = cv2.imread(imgpath)

    NIR = img[:,:,0].astype(float)
    RED = img[:,:,1].astype(float)

    nrdif = NIR - RED
    nrsum = NIR + RED

    NDVI = np.true_divide(nrdif, nrsum)


    if second_img:
        plt.close('all')
        plt.style.use('dark_background')
        hpath = msc.get_parent_dir(msc.pathWithoutFilename(outimgpath))
        mp_ndvi = os.path.join(hpath,"matplotlib_ndvi")

        mp_boxplot = os.path.join(hpath,"matplotlib_boxplot")
        mp_histog = os.path.join(hpath,"matplotlib_histog")

        msc.create_dir_ifnot_exists(mp_ndvi)
        msc.create_dir_ifnot_exists(mp_boxplot)
        msc.create_dir_ifnot_exists(mp_histog)


        hname = msc.filenameFromPathWtithoutExt(outimgpath)+"_alt.png"

        outhpath_mp_ndvi = os.path.join(mp_ndvi,hname)
        outhpath_mp_boxplot = os.path.join(mp_boxplot,hname)
        outhpath_mp_histog = os.path.join(mp_histog,hname)


        # plt.figure.c
        # fig = plt.figure()
        # ax.set_facecolor((0, 0, 0))
        plt.matshow(NDVI)
        # histog.set_facecolor("w")
        # ax = fig.add_subplot(1,1,1)

        plt.axis('off')
        plt.colorbar()
        plt.savefig(outhpath_mp_ndvi,bbox_inches='tight')

        plt.close('all')
        plt.style.use('default')
        plt.hist(NDVI.flatten(),[x for x in np.arange(-1.0,1.0,0.05)])
        plt.savefig(outhpath_mp_histog,bbox_inches='tight')

        plt.close('all')
        plt.box(NDVI.flatten().all())
        plt.savefig(outhpath_mp_boxplot)


    if print_stats and second_img:
        # parentfolder = msc.get_parent_dir(hpath)
        rep_path = os.path.join(hpath,'ndvi_stats.csv')
        print(rep_path)
        with open(rep_path,'a+') as ndvi_stats:
            statlist = list(map(str,[np.nanmax(NDVI),np.nanmin(NDVI),np.nanmean(NDVI),np.nanmedian(NDVI),np.nanquantile(NDVI,0.25),np.nanquantile(NDVI,0.75),np.nanquantile(NDVI,0.05),np.nanquantile(NDVI,0.95),np.nanquantile(NDVI,0.01),np.nanquantile(NDVI,0.99),np.nanquantile(NDVI,0.001),np.nanquantile(NDVI,0.999) ]))
            ndvi_stats.write(",".join(statlist))
            ndvi_stats.write('\n')

    # NDVI2 = np.true_divide(nrdif, nrsum, out=np.zeros_like(nrdif), where=nrsum!=0)

    if absolute_scale:
        NDVI = ((NDVI - (-1.0)) * (1/(1.0 - (-1.0)) * 255)).astype('uint8')

    else:
        NDVI = ((NDVI - np.nanmin(NDVI)) * (1/(np.nanmax(NDVI) - np.nanmin(NDVI)) * 255)).astype('uint8')


    # if print_stats:
    #         print(np.max(NDVI),np.min(NDVI),np.mean(NDVI),np.median(NDVI))

    print(outimgpath)
    cv2.imwrite(outimgpath,NDVI)

def gen_overlay_img(orig_impath,mask_impath,out_impath):
    orig_img = cv2.imread(orig_impath)
    mask_img = cv2.imread(mask_impath)

    mask_img = np.where(mask_img == np.array([255,255,255]),np.array([50,255,50]),mask_img)
    mask_img = np.where(mask_img == np.array([0,0,0]),np.array([153,153,153]),mask_img)

    output = ((0.4 * orig_img) + (0.6 * mask_img)).astype("uint8")

    cv2.imwrite(out_impath,output)


def disp_multiple(im1=None, im2=None, im3=None, im4=None):
    """
    Combines four images for display.
    """

    # code based on:
    # https://github.com/robintw/RPiNDVI/blob/master/ndvi.py (MIT LICENSE)
    # thank you, author!!

    height, width, depth = im1.shape

    combined = np.zeros((2 * height, 2 * width, 3), dtype=np.uint8)

    combined[0:height, 0:width, :] = im1 #cv2.cvtColor(im1, cv2.COLOR_GRAY2RGB)
    combined[height:, 0:width, :] =  im2 #cv2.cvtColor(im2, cv2.COLOR_GRAY2RGB)
    combined[0:height, width:, :] =  im3 #cv2.cvtColor(im3, cv2.COLOR_GRAY2RGB)
    combined[height:, width:, :] =   im4 #cv2.cvtColor(im4, cv2.COLOR_GRAY2RGB)

    return combined

def labelimg(image, text):
    """
    Labels the given image with the given text
    """
    # same author from "disp_multiple" function in this module

    return cv2.putText(image, text, (0, 50), cv2.FONT_HERSHEY_DUPLEX, 2, 255)