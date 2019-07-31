from processing_functions import color_stuff as mn 
import cv2
import glob
from processing_functions import misc as msc
import os

# impath = "/home/kauevestena/data/extracted_images/2019-06-13-15-43-38/ngr/2419.jpg"

# outpath = "/home/kauevestena/data/extracted_images/transformed/teste_b.jpg"

# mn.save_one_band(impath,outpath)

# img = cv2.imread("/home/kauevestena/testes/CamVid/test/0001TP_007170.png")
# cv2.imshow("teste",img)
# cv2.waitKey(0)


folderlist =[
    "/home/kaue/data/extracted_images/2019-07-11-16-21-46/ngr"
]

OutPthList = [
    "/home/kaue/data/extracted_images/nir_band",
    "/home/kaue/data/extracted_images/red_band"
]

for folder in folderlist:
    print(folder)
    # for filepath in glob.glob(os.path.join(folder,"*.png'")):
    # joinedpath = os.path.join(folder,"")
    for filepath in glob.glob(folder+"/*.jpg"):
        # print(filepath)
        fileName = msc.fileNumberFromPathAsStr(filepath)
        mn.save_one_band(filepath,os.path.join(OutPthList[0],fileName+'.png'),channel=0)
        mn.save_one_band(filepath,os.path.join(OutPthList[1],fileName+'.png'))


msc.telegram_bot_sendtext("band extraction terminated")