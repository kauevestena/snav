from processing_functions import validation as vd
from processing_functions import misc as msc
from processing_functions import color_stuff as cs
import os
import time
from shutil import copyfile

gen_extras = False

# epoch_path = msc.joinToHome("/data/epochs/3321/model.ckpt")
epoch_path = msc.joinToHome("data/epochs/checkpoints3/1033/model.ckpt")


# out_basepath = msc.joinToHome("/data/cnn_output")
out_basepath = msc.joinToHome("data/cnn_output3")

out_dirs = ['orig_resiz','overlay','masks','ndvi','only_veg']

msc.createDirStructure(out_basepath,out_dirs)

outpaths = {}

for name in out_dirs:
    outpaths[name] = os.path.join(out_basepath,name)


# imgs_path = "/home/kaue/data/extracted_images/2019-07-11-16-21-46/ngr"
# imgs_path = "/home/kaue/data/extracted_images/red_band"
imgs_path = "/home/kaue/data/extracted_images/newextracted"


img_list = msc.orderedFileList(imgs_path,extension='*.png')

img_list = sorted(img_list)

# del img_list[0:225]

print(img_list[0:5])

for i,img_path in enumerate(img_list):
    t1 = time.time()

    img_name = msc.fileNumberFromPathAsStr(img_path)
    out_orig = os.path.join(vd.PREDS_PATH,img_name+'.png')
    out_pred = os.path.join(vd.PREDS_PATH,img_name+'_pred.png')

    dest_orig = os.path.join(outpaths['orig_resiz'],img_name+'.png')
    dest_pred = os.path.join(outpaths['masks'],img_name+'.png')

    dest_onlyveg = os.path.join(outpaths['only_veg'],img_name+'.png')

    dest_ndvi = os.path.join(outpaths['ndvi'],img_name+'.png')
    dest_overlay = os.path.join(outpaths['overlay'],img_name+'.png')

    try:
        if not os.path.isfile(dest_pred):
            vd.single_img_forward_pass(epoch_path,img_path)

            # vd.single_img_forward_pass(epoch_path,img_path,dataset='cityscapes',model='DeepLabV3_plus')

            copyfile(out_orig,dest_orig)
            copyfile(out_pred,dest_pred)
        
        if gen_extras:
            cs.gen_only_veg_img(dest_pred,dest_orig,dest_onlyveg)
            cs.gen_uint8_NDVI(dest_onlyveg,dest_ndvi)

            cs.gen_overlay_img(dest_orig,dest_pred,dest_overlay)


    except:
        msc.telegram_bot_sendtext("failed on "+img_name)
        # msc.telegram_bot_sendtext(e)

    msc.print_rem_time_info(len(img_list),i,t1)


msc.telegram_bot_sendtext("img_gen done!!")

# cityscapes dict: /home/kaue/Semantic-Segmentation-Suite/cityscapes/class_dict.csv