#!/bin/bash

video="$1"

if [ -z "$video" ] ;  then
	echo
	echo "Please provide input video filename."
	echo
	exit 0
fi

#./darknet detector demo ./cfg/coco.data ./cfg/yolov3.cfg ./yolov3.weights "$video" -i 0 -thresh 0.25 -dont_show -out result.json
#./darknet detector test ./cfg/coco.data ./cfg/yolov3.cfg ./yolov3.weights "$video" -i 0 -thresh 0.25 -dont_show -out result.json
#./darknet detector demo ./cfg/coco.data ./cfg/yolov3.cfg ./yolov3.weights -i 0 -thresh 0.25 -dont_show -ext_output "$video"
./darknet detector demo ./cfg/coco.data ./cfg/yolov3.cfg ./yolov3.weights -i 0 -thresh 0.25 "$video"



