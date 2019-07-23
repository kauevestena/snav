import numpy as np
import cv2
from processing_functions import general_funcs as gf
from processing_functions import color_stuff as cs
from processing_functions import misc as msc
import requests
import os

import requests

def telegram_bot_sendtext(bot_message):
    
    # thx: https://is.gd/gaFK8s (Man Hay Hong)
    configFilePath  = os.path.join(os.environ['HOME'],"Dropbox/telegram_bot.txt")

    storageFile = open(configFilePath,'r')
    data = storageFile.readline()

    bot_token = data.split(',')[0]
    bot_chatID = data.split(',')[1]
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    

test = telegram_bot_sendtext("oieeeeeee")

