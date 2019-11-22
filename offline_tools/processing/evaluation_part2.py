from processing_functions import validation as vd
from tinydb import TinyDB, Query
from processing_functions import misc as msc
import os
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
import pickle


beg = time.time()

# getting DB list
db_list = vd.getDBlist()

# path of this script
scrpath = os.path.dirname(os.path.realpath(__file__))

# iterate through databases, and everything must be done here
for db_path in db_list:

    db_name = msc.filenameFromPathWtithoutExt(db_path)

    outpath = os.path.join(scrpath,'figures',db_name)

    msc.create_dir_ifnot_exists(outpath)

    db = TinyDB(db_path)
    
    ckptSet = set()
    imgSet  = set()

    for entry in db:
        ckptSet.add(entry['checkpoint'])
        imgSet.add(entry['image'])

    ckptDict = dict()

    for ckptpath in ckptSet:
        ckptDict[ckptpath] = msc.shortHash(ckptpath)


    # the default dict we can use for retrieve values, the reverse is for queries
    revCkptDict = msc.reverseDict(ckptDict)

    # print(revCkptDict)

    zeroes = np.zeros((len(ckptSet),len(imgSet)))

    # # iterating through metrics 
    # for errorMetric in vd.ONLY_METRICS:
    #     # the DataFrame
    #     df = pd.DataFrame(data=zeroes,index=list(ckptDict.values()),columns=list(imgSet))

    #     for ckpt in ckptDict:
    #         for img in imgSet:
    #             currentDict = db.search((Query().checkpoint == ckpt) & (Query().image == img))[0]
    #             # print(currentDict)
    #             df.loc[ckptDict[ckpt],img] = currentDict[errorMetric] 

    #     print(df.T)




    # first populating the storage dict with default values
    errorMetricsDfs = dict()

    defaultDf = pd.DataFrame(data=zeroes,index=list(ckptDict.values()),columns=list(imgSet))
    for errorMetric in vd.ONLY_METRICS:
        errorMetricsDfs[errorMetric] = defaultDf

    # then filling with the data itself
    for i,ckpt in enumerate(ckptDict):
        beg_it1 = time.time()
        print("stuff from {} in '{}'".format(ckpt,db_name))
        for img in imgSet:
            currentDict = db.search((Query().checkpoint == ckpt) & (Query().image == img))[0]
            for errorMetric in vd.ONLY_METRICS:
                errorMetricsDfs[errorMetric].loc[ckptDict[ckpt],img] = currentDict[errorMetric]
        msc.print_rem_time_info(len(ckptDict),i,beg_it1)
    
    for key in errorMetricsDfs:
        # print(errorMetricsDfs[key].T)

        # plotting stuff
        plt.close('all')
        plt.figure()

        picklepath = os.path.join(vd.PICKLES_PATH,key+"_"+db_name+'.pickle')

        errorMetricsDfs[key].to_pickle(picklepath,compression=None)

        errorMetricsDfs[key].plot.line()

        plt.savefig(os.path.join(outpath,key+'.png'))

        plt.close('all')
        plt.figure()

        errorMetricsDfs[key].T.plot.line()

        plt.savefig(os.path.join(outpath,'T_'+key+'.png'))


print("tooked  {} s".format(time.time()-beg))

#  TODO: PICKLE IT!!!
for key in revCkptDict:
    print("{} is {}".format(key,revCkptDict[key]))

revCkptDict_path = os.path.join(vd.PICKLES_PATH,'ckpt_rev_dict.pickle')

with open(revCkptDict_path,'wb') as pickling_dict:
    pickle.dump(revCkptDict,pickling_dict)

msc.telegram_bot_sendtext("pickled and ended!!!")
