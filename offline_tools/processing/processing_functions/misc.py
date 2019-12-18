import re
import os
import ntpath
import glob
import numpy as np
import requests
# import julian
import datetime
import time
import hashlib

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

def createDirs(dirList):
    for dirPath in dirList:
        createDir(dirPath)

def filenameFromPath(path):
    #thx https://is.gd/4331kj
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def filenameFromPathWtithoutExt(path):
    return filenameFromPath(path).split('.')[0]

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

def getSubdirs(basedir,popFirst=True):
    if not popFirst:
        return [x[0] for x in os.walk(basedir)]
    else:
        resultList = [x[0] for x in os.walk(basedir)]
        # print(resultList[0])
        del resultList[0] #otwerwise the list will include the basedir itself
        return resultList

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

def listOfLists_npArrays(inputList):
    outList = []
    for item in inputList:
        outList.append(np.array(item))
    return outList

def telegram_bot_sendtext(bot_message):
    
    # thx: https://is.gd/gaFK8s (Man Hay Hong)
    configFilePath  = os.path.join(os.environ['HOME'],"Dropbox/telegram_bot.txt")

    storageFile = open(configFilePath,'r')
    data = storageFile.readline()

    bot_token = data.split(',')[0]
    bot_chatID = data.split(',')[1]
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

def removeBasedir(path,basepath):
    return path.split(basepath)[1]

def subpathList(pathList,basepath):
    """
        return only relative subpath from a list of paths
    """

    res = []

    for path in pathList:
        res.append(removeBasedir(path,basepath))

    return res

def createDirStructure(basepath,subpaths,printPath=False):
    for subpath in subpaths:
        # print(basepath,subpath)
        finalPath = os.path.join(basepath,subpath)
        createDir(finalPath)
        if printPath:
            print(finalPath)

def getModTime(filepath):
    #thx: https://is.gd/XkIKSX 
    return datetime.datetime.fromtimestamp(os.path.getmtime(filepath))

def modFilenameExt(input,newExt='.png'):
    return fileNumberFromPathAsStr(input)+newExt
    
def get_parent_dir(path):
    return os.path.abspath(os.path.join(path, os.pardir))

def get_only_parent_dir(path):
    parent_dir = get_parent_dir(path)
    return os.path.basename(os.path.normpath(parent_dir))

def get_monitors_size():
    from screeninfo import get_monitors

    monitorslist = []
    
    for m in get_monitors():
        monitorslist.append([m.x,m.y,m.height,m.width])

    return monitorslist

def get_window_id(part_of_winname):
    return os.popen('xdotool search --onlyvisible --name '+part_of_winname).read()

def joinToHome(input_path):
    return os.path.join(os.environ['HOME'],input_path.strip('/'))

def print_rem_time_info(total_it,curent_it,ref_time):
    # "it" stands for 'iteration'
    it_time  = time.time()-ref_time
    rem_its  = total_it-curent_it
    rem_time = it_time * rem_its
    print("took {:.4f} seconds, estimated remaining time: {:.4f} minutes or {:.4f} hours, iteration {} of {}".format(it_time,rem_time/60.0,rem_time/3600.0,curent_it,total_it))

def create_dir_ifnot_exists(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)

def shortHash(inputstring,length=6,encoding='utf-8'):
    h = hashlib.shake_256()
    h.update(inputstring.encode(encoding))
    return h.hexdigest(length)

def reverseDict(inputDict):
    # thx: https://stackoverflow.com/questions/483666/reverse-invert-a-dictionary-mapping
    return {v: k for k, v in inputDict.items()}


PICKLESPATH = joinToHome('data/pickles')
