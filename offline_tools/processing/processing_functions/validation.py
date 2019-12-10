import cv2
import os
import sys
import subprocess
import numpy as np
import processing_functions.misc as msc
import processing_functions.color_stuff as cs
import pandas as pd
from tinydb import TinyDB, Query
import time


# sss imports
# sys.path.insert(0,msc.joinToHome("Semantic-Segmentation-Suite"))
# # print(sys.path)
# from utils import utils, helpers
# # from msc.joinToHome("snav/utils") import utils, helpers



# # captal letters for global variables
TINYDBS_PATH = msc.joinToHome("Dropbox/data/tinydbs/validation")
METRIC_LIST = ["checkpoint","image","accuracy", "precision", "recall", "f1", "iou"]
ONLY_METRICS = ["accuracy", "precision", "recall", "f1", "iou"]
PICKLES_PATH = msc.joinToHome("Dropbox/data/pickles/master_deg")
FIGURES_PATH = msc.joinToHome("snav/offline_tools/processing/figures")
FIGURES_PATH2 = msc.joinToHome("data/plots/master_deg")
EXECPATH = msc.joinToHome('/Semantic-Segmentation-Suite/predict.py')
SSS_PATH = msc.joinToHome('/Semantic-Segmentation-Suite')
PREDS_PATH = msc.joinToHome('/Semantic-Segmentation-Suite/preds')

# #dictonary for binaries image
# VEG_NOVEG_DICT = msc.joinToHome("/snav/configurations/class_dict.csv")
# CNL, LV = helpers.get_label_info(VEG_NOVEG_DICT)
# # num_classes = len(label_values)
# NC = len(LV)

def getDBlist():
    return msc.orderedFileList(TINYDBS_PATH,'*.json')

def calc_iou(pred,gt):
    #thx https://www.jeremyjordan.me/evaluating-image-segmentation-models/
    intersection = np.logical_and(gt, pred)
    union = np.logical_or(gt, pred)
    try:
        return np.sum(intersection) / np.sum(union)
    except:
        return 0.0



def gen_error_metrics_dict(errormetric_tuple):
    error_metrics = dict.fromkeys(METRIC_LIST)

    for i,key in enumerate(error_metrics):
        error_metrics[key] =  errormetric_tuple[i]

    return error_metrics


def error_metrics_dict(pred,gt,checkpoint,imagename,printSums = False):
    TP = 0
    TN = 0
    FP = 0
    FN = 0 

    iou = calc_iou(pred,gt)

    for i,column in enumerate(pred):
        for j,pixel in enumerate(column):
            if pixel[0] == gt[i,j,0] == 255:
                TP += 1
            elif pixel[0] == gt[i,j,0] == 0:
                TN += 1
            elif pixel[0] == 255 and gt[i,j,0] == 0:
                FP += 1
            elif pixel[0] == 0 and gt[i,j,0] == 255:
                FN += 1

    try:
        accuracy  = (TP+TN)/(TP+FP+FN+TN)
    except:
        accuracy = 0.0

    try:
        precision = (TP)/(TP+FP)
    except:
        precision = 0.0

    try:
        recall = (TP)/(TP+FN)
    except:
        recall = 0.0

    try: 
        f1 = 2*(recall * precision) / (recall + precision)
    except:
        f1 = 0.0


    if(printSums):
        print(TP,TN,FP,FN,TP+FP+FN+TN,pred.shape[0]*pred.shape[1])

    return gen_error_metrics_dict((checkpoint,imagename,accuracy,precision,recall,f1,iou))


def check_ckpt_folder(ckptfolderpath):
    checkpoint_info  = os.path.join(ckptfolderpath,'checkpoint') 
    checkpoint_model = os.path.join(ckptfolderpath,'model.ckpt.index') 

    if os.path.isfile(checkpoint_info) and os.path.isfile(checkpoint_model):
        return True
    else:
        return False

class img_and_gts:
    img_path = ""
    versions_dicts = {}

    def __init__(self, imgpath):
        self.img_path = imgpath
        self.img_name = msc.filenameFromPath(imgpath)
        self.img_number = msc.fileNumberFromPathAsStr(imgpath)

    def add_entry(self, entrypath):
        entrykey = msc.get_only_parent_dir(entrypath)
        self.versions_dicts[entrykey] = entrypath

    def print_state(self):
        print(self.img_path,'\n',self.versions_dicts)


class checkpoint:

    accepted_classnames = ['Vegetation','vegetation']

    # execpath = os.path.join(os.environ['HOME'],'/Semantic-Segmentation-Suite/predict.py'.strip('/'))
    execpath = msc.joinToHome('/Semantic-Segmentation-Suite/predict.py')

    # sss_path = os.path.join(os.environ['HOME'],'/Semantic-Segmentation-Suite'.strip('/'))
    sss_path = msc.joinToHome('/Semantic-Segmentation-Suite')

    preds_path = msc.joinToHome('/Semantic-Segmentation-Suite/preds') 

    supported_models = {"FC-DenseNet56":"FC-DenseNet56", "FC-DenseNet67":"FC-DenseNet67", "FC-DenseNet103":"FC-DenseNet103", "Encoder-Decoder":"Encoder-Decoder", "Encoder-Decoder-Skip":"Encoder-Decoder-Skip","RefineNet":"RefineNet", "FRRN-A":"FRRN-A", "FRRN-B":"FRRN-B", "MobileUNet":"MobileUNet", "MobileUNet-Skip":"MobileUNet-Skip", "PSPNet":"PSPNet", "GCN":"GCN", "DeepLabV3":"DeepLabV3", "DeepLabV3_plus":"DeepLabV3_plus", "AdapNet":"AdapNet","DenseASPP":"DenseASPP", "DDSC":"DDSC", "BiSeNet":"BiSeNet", "custom":"custom"}

    infos_suffix  = 'checkpoint'
    ckpt_suffix   = 'model.ckpt'
    patternToSearch  = 'latest_model_'
    classdict = 'class_dict.csv'

    model = ""
    dataset = ""

    error_metrics_store = {}


    outfolder = msc.joinToHome("snav/offline_tools/processing/csv")

    def __init__(self, basepath,pythonVersion='python3'):
        self.basepath = basepath
        self.infospath   = os.path.join(self.basepath,self.infos_suffix)
        self.ckpt_path = os.path.join(self.basepath,self.ckpt_suffix)
        self.running_python = pythonVersion



        with open(self.infospath) as infos:
            for line in infos:
                if self.patternToSearch in line:
                    usefulPart = line.split(self.patternToSearch)[1].split('.')[0].rsplit('_',maxsplit=1)
                    self.model   = self.supported_models[usefulPart[0]]
                    self.dataset = usefulPart[1]
                    self.dataset_classdict = os.path.join(self.sss_path,self.dataset,self.classdict)

        with open(self.dataset_classdict) as classdict:
            for line in classdict:
                for classname in self.accepted_classnames:
                    if classname in line:
                        self.veg_color_tuple = tuple(map(int,line.split('\n')[0].split(',')[1:4]))

    def process_image(self,imgpath):
        runstring = "{} {} --image {} --checkpoint {} --model {} --dataset {}".format(self.running_python,self.execpath,imgpath,self.ckpt_path,self.model,self.dataset)

        # print('runstring: {}'.format(runstring))
        subprocess.run(runstring,shell=True,cwd=self.sss_path)

    def checkIfAlreadyExists(self,img_number):
        db_list = getDBlist()

        exists = False

        for dbpath in db_list:
            db = TinyDB(dbpath)  
            if db.search((Query().checkpoint == self.ckpt_path) & (Query().image == img_number)):
                exists = True

        return exists

    def process_and_validate(self,img_gts: img_and_gts,writeImg = False,print_duration=True):
        if not self.checkIfAlreadyExists(img_gts.img_number):
            beg = time.time()

            runstring = "{} {} --image {} --checkpoint {} --model {} --dataset {}".format(self.running_python,self.execpath,img_gts.img_path,self.ckpt_path,self.model,self.dataset)

            print('runstring: {}'.format(runstring))
            subprocess.run(runstring,shell=True,cwd=self.sss_path)

            pred_path = os.path.join(self.preds_path,img_gts.img_number+'_pred.png')

            current_binarized = cs.binarize_img(pred_path,self.veg_color_tuple)
            # print(self.veg_color_tuple)

            if (writeImg):
                cv2.imwrite(os.path.join(self.preds_path,img_gts.img_number+'_bzd.png'),current_binarized)

            # creating a dict with the versions
            gt_versions = {}
            
            for key in img_gts.versions_dicts:
                gt_versions[key] = cv2.imread(img_and_gts.versions_dicts[key])

            if not self.error_metrics_store:
                for key in gt_versions:
                    self.error_metrics_store[key] = []

            # print(self.error_metrics_store)
            # doing the validation
            # the error metric dict:
            ckpt_em_dict = {} 

            for key in gt_versions:
                # gt = helpers.reverse_one_hot(helpers.one_hot_it(gt_versions[key], LV))
                # current_binarized2 = helpers.reverse_one_hot(current_binarized)
                # emTuple = utils.evaluate_segmentation(pred=current_binarized2, label=gt, num_classes=NC)
                # ckpt_em_dict[key] = error_metrics_dict(emTuple)
                # ckpt_em_dict[key] = error_metrics_dict(current_binarized,gt_versions[key],True)
                self.error_metrics_store[key].append(error_metrics_dict(current_binarized,gt_versions[key],self.ckpt_path,img_gts.img_number))

            if print_duration:
                print("it tooked {}s to run".format(time.time()-beg))


            # print(self.error_metrics_store)
            # print(ckpt_em_dict)
            # for key in gt_versions:
            #     cv2.imshow('test',gt_versions[key])
            #     cv2.waitKey(0)

            # print(gt_versions)

    # def dump_to_csvs(self):
    #     if self.error_metrics_store:
    #         try:
    #             os.makedirs(self.outfolder)
    #         except:
    #             pass
    #     for key in self.dataset_classdict:
    #         keydf = pd.DataFrame(self.dataset_classdict[key])
    #         # transform lines into lists and write'em to the files

    def dump_to_tinyDB(self):
        if not os.path.exists(TINYDBS_PATH):
            os.makedirs(TINYDBS_PATH)

        for key in self.error_metrics_store:
            dbpath = os.path.join(TINYDBS_PATH,key+".json")
            db = TinyDB(dbpath)
            for entry in self.error_metrics_store[key]:
                if not db.search((Query().checkpoint == entry['checkpoint']) & (Query().image == entry['image'])):
                    db.insert(entry)
                else:
                    print("{} not inserted".format(entry['image']))



def single_img_forward_pass(ckpt_path,img_path,model="FRRN-A",dataset='politecnico',pythonV='python3'):

    runstring = "{} {} --image {} --checkpoint {} --model {} --dataset {}".format(pythonV,EXECPATH,img_path,ckpt_path,model,dataset)
    subprocess.run(runstring,shell=True,cwd=SSS_PATH)