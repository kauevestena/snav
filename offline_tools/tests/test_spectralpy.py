import os
import glob
import random
from matplotlib import pyplot
from spectral import *


imPath = os.environ['HOME']+'/data/extracted_images/2019-06-13-15-43-38/ngr'

inputList = glob.glob(imPath+'/*.jpg')

imList = sorted(inputList,key=os.path.getmtime)

imSample = imList[random.randint(0,len(imList)-1)]
print(imSample)


img = pyplot.imread(imSample)

# img = open_image(img)

temp = SpyFile()

img = temp.load(img)

red = img.read_band(0)

nir = img.read_band(2)

vi = (nir - red) / (nir + red)

# vi = ndvi(img,2,0)

view = imshow(vi)