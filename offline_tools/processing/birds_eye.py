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
pctToCut = 45

#scale factor to be applied (10 means that pixels will be on decimeters, 100 on centimeters, and so on):
scaleFactor = 10

# print(height)
"""" ############################# """

# print(sensorDims)

# imPath = "/home/kaue/data/extracted_images/2019-06-13-15-33-34/ngr"
imPath = "/home/kaue/data/extracted_images/2019-06-13-15-43-38/ngr"

imList = sorted(glob.glob(imPath+'/*.jpg'),key=os.path.getmtime)

#reading at first some image
imSample = cv2.imread(imList[random.randint(0,len(imList)-1)])

bfs.edgeDetection(imSample,True,True)

cutted = bfs.cutImage(imSample,pctToCut)

cv2.imshow("sample",cutted)
cv2.waitKey(0)

imSize = np.flip(np.array(imSample.shape[0:2]))

# print(imSize)

# pixel size ("tp")
tp = sensorDims[0]/imSize[0]

#generating 4 points
pointsToProject = [
    bfs.pointAtPercent(imSize,0,100-pctToCut)-imSize*0.5,
    bfs.pointAtPercent(imSize,100,100-pctToCut)-imSize*0.5,
    bfs.pointAtPercent(imSize,100,100)-imSize*0.5,
    bfs.pointAtPercent(imSize,0,100)-imSize*0.5
    ]

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

for point in coordsToTransform:
    print(point)

H = cv2.findHomography()