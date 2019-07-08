# code based on:
# https://github.com/robintw/RPiNDVI/blob/master/ndvi.py (MIT LICENSE)
# thanks to the author!!

import numpy as np

from matplotlib import pyplot as plt

import cv2

# impath = "/home/kauevestena/snav/samples/0046.jpg"
impath = "/home/kauevestena/data/extracted_images/2019-06-13-15-43-38/ngr/0514.jpg"


def disp_multiple(im1=None, im2=None, im3=None, im4=None):
    """
    Combines four images for display.
    """
    height, width = im1.shape

    combined = np.zeros((2 * height, 2 * width, 3), dtype=np.uint8)

    combined[0:height, 0:width, :] = cv2.cvtColor(im1, cv2.COLOR_GRAY2RGB)
    combined[height:, 0:width, :] = cv2.cvtColor(im2, cv2.COLOR_GRAY2RGB)
    combined[0:height, width:, :] = cv2.cvtColor(im3, cv2.COLOR_GRAY2RGB)
    combined[height:, width:, :] = cv2.cvtColor(im4, cv2.COLOR_GRAY2RGB)

    return combined

def contrast_stretch(im):
    """
    Performs a simple contrast stretch of the given image, from 5-95%.
    """
    # im = im.astype('float')
    in_min = np.percentile(im, 5)
    in_max = np.percentile(im, 95)

    out_min = 0.0 # np.min(im)
    out_max = 255.0 #np.max(im)

    out = im - in_min
    out *= ((out_min - out_max) / (in_min - in_max))
    out += in_min

    return out  #.astype(np.uint8)

def label(image, text):
    """
    Labels the given image with the given text
    """
    return cv2.putText(image, text, (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)

image = cv2.imread(impath)

b, g, r = cv2.split(image)

# b = b.astype('float')
# # g = g.astype('float')
# r = r.astype('float')

bottom = (r.astype(np.float) + b.astype(np.float))
bottom[bottom == 0] = 0.00001  # Make sure we don't divide by zero!

ndvi = (b.astype(np.float) - r.astype(np.float)) / bottom

# np.savetxt('ndvi_mat.txt',ndvi)

cv2.namedWindow('ndvi',0)
cv2.imshow('ndvi',ndvi)
cv2.waitKey(0)

# ndvi = contrast_stretch(ndvi)
ndvi = ndvi.astype(np.uint8)





label(b, 'NIR')
label(g, 'something')
label(r, 'RED')
label(ndvi, 'NDVI')

# Combine ready for display
combined = disp_multiple(b, g, r, ndvi)

# Display

# combined = cv2.pyrDown(combined,combined)
# cv2.namedWindow('image',2)

cv2.namedWindow('image_raw',0)
cv2.namedWindow('image',0)

cv2.imshow('image', combined)
cv2.imshow('image_raw',image)

cv2.waitKey(0)

#snippet from: https://bit.ly/316UFvy thx Opencv Community!
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([image],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()

