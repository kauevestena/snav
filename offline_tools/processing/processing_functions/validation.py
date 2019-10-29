import cv2
import os
import sys

class checkpoint:
    supported_models = {"FC-DenseNet56":"FC-DenseNet56", "FC-DenseNet67":"FC-DenseNet67", "FC-DenseNet103":"FC-DenseNet103", "Encoder-Decoder":"Encoder-Decoder", "Encoder-Decoder-Skip":"Encoder-Decoder-Skip","RefineNet":"RefineNet", "FRRN-A":"FRRN-A", "FRRN-B":"FRRN-B", "MobileUNet":"MobileUNet", "MobileUNet-Skip":"MobileUNet-Skip", "PSPNet":"PSPNet", "GCN":"GCN", "DeepLabV3":"DeepLabV3", "DeepLabV3_plus":"DeepLabV3_plus", "AdapNet":"AdapNet","DenseASPP":"DenseASPP", "DDSC":"DDSC", "BiSeNet":"BiSeNet", "custom":"custom"}

    def __init__(self, path, model_entry):
        self.path = path
        self.model_entry = self.supported_models[model_entry]