import os
import glob
import random
from processing_functions import misc as msc
from shutil import copyfile

# define the number of samples you want
n_samples = 50


imgsPath = os.environ['HOME']+'/data/extracted_images/2019-07-11-16-21-46/ngr'


out_path = os.environ['HOME']+'/data/extracted_images/samples/'+msc.find_datetime_String(imgsPath)

# print(out_path)

msc.createDir(out_path)    




imList = msc.orderedFileList(imgsPath)

n = len(imList)
print(n)

for i in range(n_samples):
    imSample = imList[random.randint(0,n-1)]
    filename = msc.filenameFromPath(imSample)
    # print(filename)
    copyfile(imSample,os.path.join(out_path,filename))

 
print('fim')