import cv2
import os
import sys



def check_ckpt_folder(ckptfolderpath):
    checkpoint_info  = os.path.join(ckptfolderpath,'checkpoint') 
    checkpoint_model = os.path.join(ckptfolderpath,'model.ckpt.index') 

    if os.path.isfile(checkpoint_info) and os.path.isfile(checkpoint_model):
        return True
    else:
        return False

class checkpoint:
    supported_models = {"FC-DenseNet56":"FC-DenseNet56", "FC-DenseNet67":"FC-DenseNet67", "FC-DenseNet103":"FC-DenseNet103", "Encoder-Decoder":"Encoder-Decoder", "Encoder-Decoder-Skip":"Encoder-Decoder-Skip","RefineNet":"RefineNet", "FRRN-A":"FRRN-A", "FRRN-B":"FRRN-B", "MobileUNet":"MobileUNet", "MobileUNet-Skip":"MobileUNet-Skip", "PSPNet":"PSPNet", "GCN":"GCN", "DeepLabV3":"DeepLabV3", "DeepLabV3_plus":"DeepLabV3_plus", "AdapNet":"AdapNet","DenseASPP":"DenseASPP", "DDSC":"DDSC", "BiSeNet":"BiSeNet", "custom":"custom"}

    infos_suffix = 'checkpoint'
    ckpt_suffix  = 'model.ckpt'

    def __init__(self, basepath):
        self.basepath = basepath
        self.infospath   = os.path.join(self.basepath,self.infos_suffix)
        self.ckpt_suffix = os.path.join(self.basepath,self.ckpt_suffix) 




        # self.model_entry = self.supported_models[model_entry]