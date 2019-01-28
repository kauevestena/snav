#!/usr/bin/env bash

source $HOME/maplab_ws/devel/setup.bash

bagpath=$(head -n 1 $HOME/snav/configurations/current_bag.txt)

echo $bagpath

PARAMETER_FILES_PATH="$HOME/Dropbox/Mestrado/maplab/parameter_files"

LOCALIZATION_MAP_OUTPUT="$HOME/data"
ROSBAG="$bagpath"
NCAMERA_CALIBRATION="$PARAMETER_FILES_PATH/sensors.yaml"
IMU_PARAMETERS_MAPLAB="$PARAMETER_FILES_PATH/imu_maplab.yaml"
IMU_PARAMETERS_ROVIO="$PARAMETER_FILES_PATH/imu_rovio.yaml"
REST=$@

rosrun rovioli rovioli \
  --alsologtostderr=1 \
  --v=2 \
  --ncamera_calibration=$NCAMERA_CALIBRATION  \
  --imu_parameters_maplab=$IMU_PARAMETERS_MAPLAB \
  --imu_parameters_rovio=$IMU_PARAMETERS_ROVIO \
  --datasource_type="rostopic" \
  --save_map_folder="$LOCALIZATION_MAP_OUTPUT" \
  --map_builder_save_image_as_resources=false \
  --optimize_map_to_localization_map=false $REST &

  sleep 5

  xterm -hold -e rosbag play $bagpath &

