import processing_functions.color_stuff as cs 
from processing_functions import misc as msc
import csv, os

infolder = "/home/kaue/data/cnn_output3/masks"

csvpath = "/home/kaue/Dropbox/data/img_gnss.csv"

out_path = "/home/kaue/Dropbox/data/img_gnss_percent.csv"

# for imgpath in msc.orderedFileList(infolder,'*.png'):
#     print(imgpath)
#     print(cs.percentOfWhitePix(imgpath))

with open(out_path,'w+') as outfile:
    with open(csvpath) as infile:
        reader = csv.reader(infile)

        for row in reader:
            imgpath = os.path.join(infolder,row[0])

            if os.path.isfile(imgpath):
                perc = str(cs.percentOfWhitePix(imgpath))
                row.append(perc)
                outfile.write(",".join(row)+'\n')


# lat0: -49.23390

# “+proj=tmerc +lon_0=-49.23390 +k=1 +x_0=0 +y_0=0 +units=m +ellps=GRS80
# +towgs84=0,0,0,0,0,0,0 +no_defs”