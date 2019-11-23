from processing_functions import misc as msc
import os
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
import pickle
from processing_functions import validation as vd

pickles_list = msc.orderedFileList(vd.PICKLES_PATH,'*.pickle')

# print(pickles_list)

dataDict = {}

for picklepath in pickles_list:
    fname = msc.filenameFromPathWtithoutExt(picklepath)
    print(fname)
    with open(picklepath,'rb') as picklefile:
        dataDict[fname] = pickle.load(picklefile)

# print(dataDict)

ckpts_dict = dict(dataDict['ckpt_rev_dict'])

del dataDict['ckpt_rev_dict']


for key in dataDict:

    # print(dataDict[key][list(ckpts_dict.keys())[0]])
    df = dataDict[key].T
    # df.T.iloc[0,:].plot.line()
    # print()

    outdir = os.path.join(vd.FIGURES_PATH2,"metrics_per_img",key)
    msc.create_dir_ifnot_exists(outdir)

    print(key)
    for index,row in df.iterrows():
            # print(index)
            # print(row)
            plt.close('all')
            plt.figure()
            row.plot()
            plt.savefig(os.path.join(outdir,index+'.png'))
