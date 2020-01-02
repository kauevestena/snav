# from processing_functions import color_stuff as cs
from processing_functions import misc as msc 
# from processing_functions import general_funcs as gf
import os
# import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


stats_path = "/home/kaue/data/cnn_output/ndvi_stats.csv"


dataframe = pd.read_csv(stats_path)

# dataframe.remove

dataframe.drop(columns=['mean','q0.1%','q99.9%','q1%','q99%']).plot()

plt.savefig(msc.joinToHome("data/ndvi_stats.png"),bbox_inches='tight',dpi=300)

dataframe.drop(columns=['mean','max','min','q0.1%','q99.9%']).plot()

plt.savefig(msc.joinToHome("data/ndvi_stats2.png"),bbox_inches='tight',dpi=300)

print(dataframe.mean())
print(dataframe.median())
print(dataframe.std())