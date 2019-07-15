import re
import os
import ntpath
import glob

def find_datetime_String(inputStr,onlyDate=False):
    if onlyDate:
        date = re.search('\d{4}-\d{2}-\d{2}',inputStr)
    else:
        date = re.search('\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}',inputStr)
    
    return date.group()

def createDir(dirPath):
    try:
        os.makedirs(dirPath)
    except:
        pass

def filenameFromPath(path):
    #thx https://is.gd/4331kj
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def orderedFileList(imPath,extension='*.jpg'):
    print(os.path.join(imPath,extension))
    return sorted(glob.glob(os.path.join(imPath,extension)),key=os.path.getmtime)