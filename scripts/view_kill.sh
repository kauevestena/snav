#!/bin/bash

source /home/ubuntu/snav_ws/devel/setup.bash

rosnode kill $(rosnode list | grep image_view)