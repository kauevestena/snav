import cv2
import numpy as np

def teste():
    print("teste")

def imDims(img):
    return np.flip(np.array(img.shape[0:2]))

def checkPercent(percent):
    if percent <= 100 and percent >= 0:
        return True
    else:
        return False

def percentRound(dimension,percent):
    return int(round(dimension*(percent/100.0)))

def cutImage(image,percent):
    if not checkPercent(percent):
        return image
    else:
        imSize = np.array(image.shape[0:2])
        newHeight = percentRound(imSize[0],percent)
        return image[imSize[0]-newHeight:,:]

def pointAtPercent(imSize,pCol,pRow):
    if (not checkPercent(pCol)) or (not checkPercent(pRow)):
        return np.array([-1,-1])
    else:
        x = percentRound(imSize[0],pCol)
        y = percentRound(imSize[1],pRow)
        return np.array([x,y])

def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0: 
       return v
    print(v*1/norm)
    return v * (1/norm)

def linePlaneIntersection(lineP,planeP,lineDVec,planeNVec):
    dUp   = np.dot(planeP-lineP,planeNVec)
    dDown = np.dot(planeNVec,lineDVec) 
    d = (dUp/dDown)
    return d*lineDVec

def ggbpoint(point,string=False):
    strPoint = "("+str(point[0])+","+str(point[1])+","+str(point[2])+")"
    if string:
        return strPoint
    else:
        print(strPoint)

# def base100(value):
#     if (abs(value) < 100):
#         while (abs(value) < 100):
#             value*=10
#     else:
#         while (abs(value) > 100 and abs(value) < 1000):
#             value/=10
#     return round(value)

def pMat_to_List(pointsMat):
    pointList=[]

    for line in range(np.size(pointsMat,axis=0)):
        pointList.append(pointsMat[line,:])

    return pointList

def minOfPointList(pointList):
    pointsMat = np.array(pointList)
    return np.min(pointsMat,axis=0)

def maxOfPointList(pointList):
    pointsMat = np.array(pointList)
    return np.max(pointsMat,axis=0)

def listOfPointsXscalar(pointList,scalar):
    return pMat_to_List(np.array(pointList)*scalar)

def prepareListOfPoints(pointList,scaleFactor):
    mins      = minOfPointList(pointList)
    newList = []
    for point in pointList:
        newList.append(point-mins)
    
    maxx = np.max(maxOfPointList(newList))
    # print(maxx)
    return listOfPointsXscalar(newList,scaleFactor)

def removePListYcoord(inputList):
    asMat = np.array(inputList)[:,[0,2]]
    return pMat_to_List(asMat)

def edgeDetection(image,showImg=False,showStack=False):
    ### thx: https://blog.sicara.com/opencv-edge-detection-tutorial-7c3303f10788 (modified)
    # Converting the image to grayscale.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    r,rnir,nir = cv2.split(image)
    gray = nir

    # Smoothing without removing edges.
    # gray_filtered = cv2.bilateralFilter(gray, 25, 10, 10)
    gray_filtered = gray

    # Applying the canny filter
    edges_filtered = cv2.Canny(gray_filtered, 60, 120)

    if showImg and not showStack:
        cv2.imshow("canny edges",edges_filtered)
        cv2.waitKey(0)
    elif showImg and showStack:
        cv2.namedWindow("canny edges",0)
        images = np.hstack((gray_filtered, edges_filtered))
        cv2.imshow("canny edges",images)
        cv2.waitKey(0)

    return edges_filtered

def addOnes(pointArray):
    result = []
    for point in pointArray:
        result.append(np.append(point,np.array([1])))
    return result

def transformListOfPtsPerspective(listOfPoints,transformation):
    """ the function spects that the transformation is a 3x3 matrix """
    listOfPoints = addOnes(listOfPoints)
    transformed = []
    for point in listOfPoints:
        temp = np.matmul(transformation,point)
        temp = np.array([temp[0]/temp[2],temp[1]/temp[2]])
        transformed.append(temp)
    return transformed