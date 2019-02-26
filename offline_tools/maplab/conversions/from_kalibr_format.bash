#!/bin/bash


#  /home/kauevestena/Dropbox/Mestrado/Calibracao_cameras/kalibr/resultados/pi_cam/camchain-imucam-homekauedatakalibr_bagsdynamic2019-02-21-17-44-23.yaml

rosrun kalibr kalibr_maplab_config --to-ncamera \
    --label snav \
    --cam $1