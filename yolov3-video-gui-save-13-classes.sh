#!/bin/bash

video="$1"

if [ -z "$video" ] ;  then
	echo
	echo "Please provide input video filename."
	echo
	exit 0
fi

./darknet detector demo ./cfg/coco.data ./cfg/yolov3.cfg ./yolov3.weights -i 0 -thresh 0.25 "$video" -min_prob_to_save 85 -saved_classes dog,person,ball,truck,car,bike,chair,armoire,motorbike,cat,plane,elicopter,tree


