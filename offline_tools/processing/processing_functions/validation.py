import cv2
import os
import sys
import subprocess
import processing_functions.misc as msc
import processing_functions.color_stuff as cs


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


    def __init__(self, basepath):
        self.basepath = basepath
        self.infospath   = os.path.join(self.basepath,self.infos_suffix)
        self.ckpt_path = os.path.join(self.basepath,self.ckpt_suffix) 



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
        runstring = "python3 {} --image {} --checkpoint {} --model {} --dataset {}".format(self.execpath,imgpath,self.ckpt_path,self.model,self.dataset)

        # print('runstring: {}'.format(runstring))
        subprocess.run(runstring,shell=True,cwd=self.sss_path)


    def process_and_validate(self,img_gts: img_and_gts):
        runstring = "python3 {} --image {} --checkpoint {} --model {} --dataset {}".format(self.execpath,img_gts.img_path,self.ckpt_path,self.model,self.dataset)

        print('runstring: {}'.format(runstring))
        subprocess.run(runstring,shell=True,cwd=self.sss_path)

        pred_path = os.path.join(self.preds_path,img_gts.img_number+'_pred.png')

        current_binarized = cs.binarize_img(pred_path,self.veg_color_tuple)
        print(self.veg_color_tuple)

        cv2.imwrite(os.path.join(self.preds_path,img_gts.img_number+'_bzd.png'),current_binarized)







        