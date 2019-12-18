from processing_functions import misc as msc
from processing_functions import general_funcs as gf

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
    # print(fname)
    with open(picklepath,'rb') as picklefile:
        dataDict[fname] = pickle.load(picklefile)

# print(dataDict)

ckpts_dict = dict(dataDict['ckpt_rev_dict'])

del dataDict['ckpt_rev_dict']


for key in dataDict:
    print(key)

    # # # # # GENERATING CHARTS FOR THE METRICS PER IMG:
    # df = dataDict[key].T
    # outdir = os.path.join(vd.FIGURES_PATH2,"metrics_per_img",key)
    # msc.create_dir_ifnot_exists(outdir)

    # print(key)
    # for index,row in df.iterrows():
    #         # print(index)
    #         # print(row)
    #         plt.close('all')
    #         plt.figure()
    #         row.plot()
    #         plt.savefig(os.path.join(outdir,index+'.png'))

    # # # # # # GENERATING CHARTS FOR THE METRICS PER EPOCH:
    # df = dataDict[key]
    # outdir = os.path.join(vd.FIGURES_PATH2,"metrics_per_epoch",key)
    # msc.create_dir_ifnot_exists(outdir)

    # # print(key)
    # for index,row in df.iterrows():
    #         print(index)
    #         # print(index)
    #         # print(row)
    #         plt.close('all')
    #         plt.figure()
    #         row.plot()
    #         plt.savefig(os.path.join(outdir,index+'.png'))

    # # # # # GENERATING HISTS FOR THE METRICS PER IMG:
    # outdir = os.path.join(vd.FIGURES_PATH2,"hist_metrics_per_img",key)
    # gf.gen_charts_per_row(dataDict[key],outdir,"histogram",True)

    # # # # # GENERATING HISTS FOR THE METRICS PER EPOCH:
    # outdir = os.path.join(vd.FIGURES_PATH2,"hist_metrics_per_epoch",key)
    # gf.gen_charts_per_row(dataDict[key],outdir,"histogram")

    # # # # # GENERATING HISTS FOR THE METRICS PER EPOCH:
    # outdir = os.path.join(vd.FIGURES_PATH2,"hist_metrics_per_epoch",key)
    # gf.gen_charts_per_row(dataDict[key],outdir,"histogram")


    # # # # GENERATING BOXPLOTS FOR THE METRICS PER EPOCH:
    outdir = os.path.join(vd.FIGURES_PATH2,"boxplots_per_epoch",key)
    gf.gen_charts_per_row(dataDict[key],outdir,"boxplot")

    # # # # GENERATING BOXPLOTS FOR THE METRICS PER IMG:
    outdir = os.path.join(vd.FIGURES_PATH2,"boxplots_per_img",key)
    gf.gen_charts_per_row(dataDict[key],outdir,"boxplot",True)

    # # # # GENERATING DENSITY CHARTS FOR THE METRICS PER EPOCH:
    outdir = os.path.join(vd.FIGURES_PATH2,"density_charts_per_epoch",key)
    gf.gen_charts_per_row(dataDict[key],outdir,"density")

    # # # # GENERATING DENSITY CHARTS FOR THE METRICS PER IMG:
    outdir = os.path.join(vd.FIGURES_PATH2,"density_charts_per_img",key)
    gf.gen_charts_per_row(dataDict[key],outdir,"density",True)