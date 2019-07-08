import cv2

def save_one_band(imPath,outPath,channel=2):
    """
        to save only one band, generally the red band
    """
    splitted = []
    img = cv2.imread(imPath)
    splitted = cv2.split(img)
    cv2.imwrite(outPath,splitted[channel])