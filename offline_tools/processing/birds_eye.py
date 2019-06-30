# constants
import cv2
import glob
import random
import numpy as np
import os
from processing_functions import birdsfuncs as bfs

# # path="/home/kaue/snav/offline_tools/processing"
# # os.chdir(path)

""" CONSTANTS """

# sensor size
sensorDims = np.array((0.00368,0.00276))
# focal distance
f = 0.00291323
# height
hcar   = 1.487
hplat  = 0.15
height = hcar+hplat

#percentual to cut
pctToCut = 35

#scale factor to be applied (10 means that pixels will be on decimeters, 100 on centimeters, and so on):
scaleFactor = 100

# print(height)
"""" ############################# """

# print(sensorDims)

# imPath = "/home/kaue/data/extracted_images/2019-06-13-15-33-34/ngr"
imPath = "/home/kaue/data/extracted_images/2019-06-13-15-43-38/ngr"

imList = sorted(glob.glob(imPath+'/*.jpg'),key=os.path.getmtime)

#reading at first some image
imSample = cv2.imread(imList[random.randint(0,len(imList)-1)])

# bfs.edgeDetection(imSample,True,True)

cutted = bfs.cutImage(imSample,pctToCut)

# print(imSample.shape)
# print(cutted.shape)

cv2.imshow("sample",cutted)
cv2.waitKey(0)

imSize = bfs.imDims(imSample)

imCutSize = bfs.imDims(cutted)

print(imCutSize)

# pixel size ("tp")
tp = sensorDims[0]/imSize[0]

#generating 4 points

pointsToProject0 = [
    bfs.pointAtPercent(imSize,0,100-pctToCut),
    bfs.pointAtPercent(imSize,100,100-pctToCut),
    bfs.pointAtPercent(imSize,100,100),
    bfs.pointAtPercent(imSize,0,100)
    ]

pointsToProject = pointsToProject0 - imSize*0.5

pointsToProjectMeters = []
for point in pointsToProject:
    pointsToProjectMeters.append(point*tp)

# for point in pointsToProjectMeters:
#     bfs.ggbpoint(np.append(point,f))

#lines as their direction vectors, they cointains the origin
linesToProject = []
for point in pointsToProjectMeters:
    # linesToProject.append(bfs.normalize(np.append(point,f)))
    linesToProject.append(np.append(point,f))

planeNorm = np.array([0,1,0])
planePt = np.array([10,height,10])

projPoints = []
for vector in linesToProject:
    projPoints.append(bfs.linePlaneIntersection(vector,planePt,vector,planeNorm))

coordsToTransform = bfs.prepareListOfPoints(projPoints,scaleFactor)
coordsToTransform = bfs.removePListYcoord(coordsToTransform)


pointsToProjectCut = [
    bfs.pointAtPercent(imCutSize,0,0),
    bfs.pointAtPercent(imCutSize,100,0),
    bfs.pointAtPercent(imCutSize,100,100),
    bfs.pointAtPercent(imCutSize,0,100)
    ]

for i in range(len(coordsToTransform)):
    # print(coordsToTransform[i],pointsToProjectCut[i])
    print((coordsToTransform[i][0],coordsToTransform[i][1]))

H = cv2.findHomography(np.array(pointsToProjectCut),np.array(coordsToTransform),0)


# temp = bfs.addOnes(pointsToProjectCut)
# temp = np.array(temp)

# # print(cv2.perspectiveTransform(temp,H[0]))


transformedPtSample = bfs.transformListOfPtsPerspective(pointsToProjectCut,H[0])

outSize = np.array(bfs.maxOfPointList(transformedPtSample),dtype='uint16')

print(outSize)

transformedCut = cv2.warpPerspective(cutted,H[0],tuple(outSize))
cv2.namedWindow("warped",0)
cv2.imshow("warped",transformedCut)
cv2.waitKey(0)