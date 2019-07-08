import os
import sys

""" originally created for use with this repo: https://github.com/GeorgeSeif/Semantic-Segmentation-Suite  """

folders = ['train','train_labels','val','val_labels','test','test_labels']

print(sys.argv)

if len(sys.argv) == 2:
    basepath = sys.argv[1]
    for folder in folders:
        fullpath = os.path.join(basepath,folder)
        try:
            os.makedirs(fullpath)
        except:
            pass
else:
    print("insert the basepath name!")