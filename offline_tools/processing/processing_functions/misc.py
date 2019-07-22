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

def pathWithoutFilename(path):
    head, tail = ntpath.split(path)
    return head

def orderedFileList(imPath,extension='*.jpg',option=0,printPath=False):
    """
    creates an ordered filelist from the input path

    option: 0 to sort by modtime, 1 to sort by name
    """
    if printPath:
        print(os.path.join(imPath,extension))

    if option == 0:
        return sorted(glob.glob(os.path.join(imPath,extension)),key=os.path.getmtime)
    if option == 1:
        return sorted(glob.glob(os.path.join(imPath,extension)))

def getSubdirs(basedir):
    return [x[0] for x in os.walk(basedir)]

def checkForImages(inputPath,extension='*.jpg'):
    listOfPath = glob.glob(os.path.join(inputPath,extension))
    if listOfPath == []:
        return False
    else:
        return True

def fileNumberFromPath(filePath):
    fileName = filenameFromPath(filePath)
    return int(fileName.split('.')[0])

def fileNumberFromPathAsStr(filePath):
    fileName = filenameFromPath(filePath)
    return fileName.split('.')[0]

def writeToFile(filePath,stringToWrite):
    storageFile = open(filePath,'w')
    storageFile.write(stringToWrite)
    storageFile.close()

def readNumberFromFile(filePath):
    storageFile = open(filePath,'r')
    number = int(storageFile.readline())
    storageFile.close()
    return number