from processing_functions import misc as msc
from processing_functions import general_funcs as gf

import os
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
import pickle
from processing_functions import validation as vd

######
from PIL import Image

def add_img_outline(imgpath,print_dimensions=True):

    # many thx: https://stackoverflow.com/a/11143078/4436950
    image = Image.open(imgpath)
    w,h = image.size
    new_w = w + int(float(w)/250)
    new_h = h + int(float(h)/250)
    
    if print_dimensions:
        print(w,h,new_w,new_h)

    new_size = (new_w,new_h)
    new_image = Image.new("RGB",new_size)
    new_image.paste(image,((new_size[0]-image.size[0])//2,(new_size[1]-image.size[1])//2))
    new_image.save(imgpath.replace('.png','_outline.png'))


#######

# naming for the local folder:
outlocalfolder = "phase3_reloaded"

pickles_list = msc.orderedFileList(vd.PICKLES_PATH,'*.pickle')

t1 = time.time()

#print(pickles_list)

dataDict = {}

for picklepath in pickles_list:
    fname = msc.filenameFromPathWtithoutExt(picklepath)
    #print(fname)
    with open(picklepath,'rb') as picklefile:
        dataDict[fname] = pickle.load(picklefile)

#print(dataDict)

ckpts_dict = dict(dataDict['ckpt_rev_dict'])

del dataDict['ckpt_rev_dict']

ckpts_dict_2 = {}

for key in ckpts_dict:
    ckpts_dict_2[key] = msc.get_only_parent_dir(ckpts_dict[key])

#print(ckpts_dict_2)

#print(dataDict)

for key in dataDict:
    pass
    #print()

idxmin_cityscapes = []

# first of all: defining the epochs that will really be used:
for key in dataDict:
    dataDict[key] = dataDict[key].rename(index=ckpts_dict_2).sort_index().T

    if key == "iou_with_terrain_veg":
        mins = dataDict[key].mean().nsmallest(3)
        idxmin_cityscapes = list(mins.index)
        lastidx = "0"+str(int(idxmin_cityscapes[-1]))
        idx_list = list(dataDict[key].columns)
        #print(idx_list)
        lastidx = idx_list[idx_list.index(lastidx)-1]
        #print(lastidx)


    elif key == "iou_new_validation":
        mins = dataDict[key].mean().nsmallest(1)
        idxmin_own= list(mins.index)

#print(idxmin_cityscapes,idxmin_own,lastidx)    



# subdividing the dataframes:
for key in dataDict:
    #print(dataDict[key])
    if "only_trees" in key or "with_terrain_veg" in key:
        dataDict[key].drop(columns=idxmin_cityscapes,inplace=True)
        idx_list = list(dataDict[key].columns)
        #print(idx_list)
        split_index = idx_list.index(lastidx)
        dataDict[key] = dataDict[key].iloc[:,:split_index]

        curr_cols = list(dataDict[key].columns)
        curr_cols = list(map(int,curr_cols))
        curr_cols = [val+100 for val in curr_cols]
        curr_cols = [str(val).zfill(4) for val in curr_cols]
        dataDict[key].columns = curr_cols




    elif "new_validation" in key:
        idx_list = list(dataDict[key].columns)
        split_index = idx_list.index(idxmin_own[0])
        dataDict[key] = dataDict[key].iloc[:,split_index:]
        
        curr_cols = list(dataDict[key].columns)
        curr_cols = list(map(int,curr_cols))
        curr_cols = [val-min(curr_cols) for val in curr_cols]
        curr_cols = [str(val).zfill(4) for val in curr_cols]

        dataDict[key].columns = curr_cols

        #print(curr_cols)



current_metric = "mean_epochs_stats"
c_dpi = 900

#print("took",time.time()-t1,"seconds")

# dict for best epochs summary 
summary_df_dict = {}

# list of rows with best error metrics
best_epochs_idx = []

for i,key in enumerate(dataDict):


    print(key)

    newdf = dataDict[key]

    print(newdf.head())

    mean = newdf.mean()
    std  = newdf.std()
    stderrmean = newdf.sem() 
    dfmin  = newdf.min()
    dfmax = newdf.max()
    plstd = mean + std
    mnstd = mean - std

    statsdf = pd.concat([dfmax,plstd,mean,mnstd,dfmin],axis=1)
    # for pt-br:
    # statsdf.columns = ['máx.','méd.+d.p.','média','méd.-d.p','mín.']
    # for en:
    statsdf.columns = ['max.','mean+s.d.','mean','mean-s.d.','min.']



    #print(statsdf)
    #print(std)
    # #print(key,key.split("_")[0])
    outdir = os.path.join(vd.FIGURES_PATH2,outlocalfolder,current_metric)
    msc.create_dir_ifnot_exists(outdir)
    figname = os.path.join(outdir,key+"_"+current_metric+".png")
    figname_t = os.path.join(outdir,key+"_"+current_metric+"_T.png")

    statsdf.plot(style=['-g',':c','-b',':c','-r'],markersize = 2)

    # for pt-br
    # plt.ylabel('Valor (%)')
    # plt.xlabel('Número da Época')
    # for en 
    plt.ylabel('Value')
    plt.xlabel('Epoch')



    plt.savefig(figname,dpi=c_dpi)
    add_img_outline(figname)
    plt.close('all')

    #print('\n',newdf.head())

    bestepochidx = statsdf['mean'].idxmax()    
    #print(statsdf.T[bestepochidx])


    best_epochs_idx.append(bestepochidx)

    median = newdf.median()
    kurt   = newdf.kurtosis()
    skewn = newdf.skew()

    statsdf2 = pd.concat([dfmax,median,dfmin,mean,std,stderrmean],axis=1)
    # for pt-br
    # statsdf2.columns = ['máx.','mediana','mín.','média','desv. pad','d.p. média']
    # for en
    statsdf2.columns = ['max.','median','min.','mean','std. dev.','s.d. mean']


    summary_df_dict[key] = statsdf2.T[bestepochidx]

    #print(newdf.columns)

    #print(statsdf2.T[bestepochidx])
    #print(statsdf2)


# summary of best error metrics
summary_df = pd.DataFrame(summary_df_dict)
summary_df.to_csv(msc.joinToHome("Dropbox/data/best_em_summary.csv"))




#print(best_epochs_idx)

best_epochs_metrics = []

for i,key in enumerate(dataDict):
    if i < 10:
        best_epochs_metrics.append(dataDict[key][best_epochs_idx[0]])
    else:
        best_epochs_metrics.append(dataDict[key][best_epochs_idx[-1]])

    #print(i)

#print(best_epochs_metrics)

fignames = ['with_terrain.png','only_trees.png','my_dataset.png']

current_metric = "boxplots"
outdir = os.path.join(vd.FIGURES_PATH2,outlocalfolder,current_metric)
msc.create_dir_ifnot_exists(outdir)

j = 0
for i in range(0,len(best_epochs_metrics),5):

    print(current_metric)
    figpath = os.path.join(outdir,fignames[j])

    curr_df = pd.concat(best_epochs_metrics[i:i+5],axis=1)
    # for pt-br
    # curr_df.columns = ['T.A','V.P.P.','Sens.','F1','IoU']
    curr_df.columns = ['H.R.','P.P.V.','Sens.','F1','IoU']

    ax =   curr_df.boxplot(grid=False,showmeans=True,meanprops={"marker":'o','markerfacecolor':'r'})

    # print(ax)
    # for pt-br
    # plt.ylabel('Valor (%)')
    # plt.xlabel('Métrica')
    # for en
    plt.ylabel('Value')
    plt.xlabel('Metric')

    #print(type(ax))

    plt.tight_layout()

    #print(figpath)
    #print(curr_df)
    plt.savefig(figpath,dpi=c_dpi)
    add_img_outline(figpath)
    plt.close('all')

    j += 1


# im just tired, so I will really just copy the snippet:

current_metric = "best_epoch_lines"
outdir = os.path.join(vd.FIGURES_PATH2,outlocalfolder,current_metric)
msc.create_dir_ifnot_exists(outdir)

j = 0
for i in range(0,len(best_epochs_metrics),5):
    print(current_metric)


    figpath = os.path.join(outdir,fignames[j])

    curr_df = pd.concat(best_epochs_metrics[i:i+5],axis=1)
    # for pt-br
    # curr_df.columns = ['T.A','V.P.P.','Sens.','F1','IoU']
    curr_df.columns = ['H.R.','P.P.V.','Sens.','F1','IoU']

    ax =   curr_df.sort_values(curr_df.columns[4]).plot()

    # for pt-br
    # plt.ylabel('Valor (%)')
    # plt.xlabel('Número da Fotografia')
    # for en
    plt.ylabel('Value')
    plt.xlabel('Photo Number')

    #print(type(ax))

    #print(figpath)
    ##print(curr_df)
    plt.savefig(figpath,dpi=c_dpi)
    add_img_outline(figpath)
    plt.close('all')

    j += 1

current_metric = "histograms"
outdir = os.path.join(vd.FIGURES_PATH2,outlocalfolder,current_metric)
msc.create_dir_ifnot_exists(outdir)

j = 0
for i in range(0,len(best_epochs_metrics),5):
    print(current_metric)


    figpath = os.path.join(outdir,fignames[j])

    curr_df = pd.concat(best_epochs_metrics[i:i+5],axis=1)
    # for pt-br
    # curr_df.columns = ['T.A','V.P.P.','Sens.','F1','IoU']
    curr_df.columns = ['H.R.','P.P.V.','Sens.','F1','IoU']

    ax =   curr_df.plot.hist(alpha=0.8)
    plt.ylabel('count')
    plt.xlabel('values')

    # plt.setp(plt.gcf(),edgecolor='k')
    # plt.Figure.set_ed
    ##print(type(ax))

    ##print(figpath)
    ##print(curr_df)
    plt.savefig(figpath,dpi=c_dpi)
    add_img_outline(figpath)
    plt.close('all')

    j += 1


"""
best epochs:

 ['0200', '0121', '0125', '0200', '0200', '0200', '0121', '0200', '0200', '0200', '0984', '0909', '0930', '1059', '1059'] 

constants removed:

['0040', '0201', '0200'] ['2271'] 0120

"""

# # for key in dataDict:
# #     #print(key)

# #     # # # # # GENERATING CHARTS FOR THE METRICS PER IMG:
# #     # df = dataDict[key].T
# #     # outdir = os.path.join(vd.FIGURES_PATH2,"metrics_per_img",key)
# #     # msc.create_dir_ifnot_exists(outdir)

# #     # #print(key)
# #     # for index,row in df.iterrows():
# #     #         # #print(index)
# #     #         # #print(row)
# #     #         plt.close('all')
# #     #         plt.figure()
# #     #         row.plot()
# #     #         plt.savefig(os.path.join(outdir,index+'.png'))

# #     # # # # # # GENERATING CHARTS FOR THE METRICS PER EPOCH:
# #     # df = dataDict[key]
# #     # outdir = os.path.join(vd.FIGURES_PATH2,"metrics_per_epoch",key)
# #     # msc.create_dir_ifnot_exists(outdir)

# #     # # #print(key)
# #     # for index,row in df.iterrows():
# #     #         #print(index)
# #     #         # #print(index)
# #     #         # #print(row)
# #     #         plt.close('all')
# #     #         plt.figure()
# #     #         row.plot()
# #     #         plt.savefig(os.path.join(outdir,index+'.png'))

# #     # # # # # GENERATING HISTS FOR THE METRICS PER IMG:
# #     # outdir = os.path.join(vd.FIGURES_PATH2,"hist_metrics_per_img",key)
# #     # gf.gen_charts_per_row(dataDict[key],outdir,"histogram",True)

# #     # # # # # GENERATING HISTS FOR THE METRICS PER EPOCH:
# #     # outdir = os.path.join(vd.FIGURES_PATH2,"hist_metrics_per_epoch",key)
# #     # gf.gen_charts_per_row(dataDict[key],outdir,"histogram")

# #     # # # # # GENERATING HISTS FOR THE METRICS PER EPOCH:
# #     # outdir = os.path.join(vd.FIGURES_PATH2,"hist_metrics_per_epoch",key)
# #     # gf.gen_charts_per_row(dataDict[key],outdir,"histogram")


# #     # # # # GENERATING BOXPLOTS FOR THE METRICS PER EPOCH:
# #     outdir = os.path.join(vd.FIGURES_PATH2,"boxplots_per_epoch",key)
# #     gf.gen_charts_per_row(dataDict[key],outdir,"boxplot")

# #     # # # # GENERATING BOXPLOTS FOR THE METRICS PER IMG:
# #     outdir = os.path.join(vd.FIGURES_PATH2,"boxplots_per_img",key)
# #     gf.gen_charts_per_row(dataDict[key],outdir,"boxplot",True)

# #     # # # # GENERATING DENSITY CHARTS FOR THE METRICS PER EPOCH:
# #     outdir = os.path.join(vd.FIGURES_PATH2,"density_charts_per_epoch",key)
# #     gf.gen_charts_per_row(dataDict[key],outdir,"density")

# #     # # # # GENERATING DENSITY CHARTS FOR THE METRICS PER IMG:
# #     outdir = os.path.join(vd.FIGURES_PATH2,"density_charts_per_img",key)
# #     gf.gen_charts_per_row(dataDict[key],outdir,"density",True)


#print(ckpts_dict)

#print(len(ckpts_dict))