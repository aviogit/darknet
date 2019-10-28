#!/bin/bash

video="$1"

if [ -z "$video" ] ;  then
	echo
	echo "Please provide input video filename."
	echo
	exit 0
fi

./darknet detector demo ./cfg/coco.data ./cfg/yolov3.cfg ./yolov3.weights -i 0 -thresh 0.25 -dont_show -ext_output "$video"



