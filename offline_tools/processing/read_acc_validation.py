from processing_functions import misc as msc
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

plt.close('all')

def joinFixedFilename1(inputpath):
    return os.path.join(inputpath,'val_scores.csv')

checkpointsFolder = "/media/kauevestena/data/Semantic-Segmentation-Suite/checkpoints"

checkpointdirlist = sorted(msc.getSubdirs(checkpointsFolder,popFirst=True))

val_scores_list = list(map(joinFixedFilename1,checkpointdirlist))

# print(val_scores_list)

# print(checkpointdirlist)

outDf = pd.DataFrame()

for i,val_score_file in enumerate(val_scores_list):
    vegetation_acc = pd.read_csv(val_score_file,)

    # if i < 2:
    #     print(vegetation_acc[' vegetation'])

    # if i < 3:
    outDf[i]=(vegetation_acc[' vegetation'])
    
# outDf.replace(1.0,float('nan'))


# df1['A'] = df1['A'].apply(lambda x: [y if y <= 9 else 11 for y in x])


outDf = outDf.apply(lambda x: [y if y < 0.9999999999999 else float('nan') for y in x])

# print(matplotlib.get_backend())

outDf = outDf.transpose()

plt.figure()

outDf.plot.line(subplots=True)

print(outDf)

scrpath = os.path.dirname(os.path.abspath(__file__))

plt.savefig(os.path.join(scrpath,'figures/evolution.png'))