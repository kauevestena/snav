import os

home = os.environ['HOME']

inputPath = home+"/data/extracted_images/2019-06-13-15-43-38"

outPath = os.path.join(home,"tests/mappilary_cnn_01")

#space
s = " "

modelpath = "/home/kaue/Downloads/wide_resnet38_deeplab_vistas.pth.tar"

scriptPath = os.path.join(home,"inplace_abn/scripts/test_vistas.py")

try:
    os.makedirs(outPath)
except:
    pass

inputPath = home+"/data/extracted_images/2019-06-13-15-43-38"

runString = "python3"+s+scriptPath+s+modelpath+s+inputPath+s+outPath

print(runString)

os.system("cd "+"/home/kaue/inplace_abn/scripts")
os.system(runString)
