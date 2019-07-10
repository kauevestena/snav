from processing_functions import monochrome as mn 
import cv2
import glob
import os

# impath = "/home/kauevestena/data/extracted_images/2019-06-13-15-43-38/ngr/2419.jpg"

# outpath = "/home/kauevestena/data/extracted_images/transformed/teste_b.jpg"

# mn.save_one_band(impath,outpath)

# img = cv2.imread("/home/kauevestena/testes/CamVid/test/0001TP_007170.png")
# cv2.imshow("teste",img)
# cv2.waitKey(0)


folderlist =[
    "/home/kauevestena/testes/CamVid/test",
    "/home/kauevestena/testes/CamVid/train",
    "/home/kauevestena/testes/CamVid/val"
]

for folder in folderlist:
    print(folder)
    # for filepath in glob.glob(os.path.join(folder,"*.png'")):
    # joinedpath = os.path.join(folder,"")
    for filepath in glob.glob(folder+"/*.png"):
        # print(filepath)
        mn.save_one_band(filepath,filepath)
