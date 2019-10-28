#!/bin/bash

video="$1"

if [ -z "$video" ] ;  then
	echo
	echo "Please provide input video filename."
	echo
	exit 0
fi

./darknet detector demo ./cfg/coco.data ./cfg/yolov3.cfg ./yolov3.weights -i 0 -thresh 0.25 "$video" -min_prob_to_save 85 -saved_classes apple,backpack,banana,bear,bed,bench,bicycle,bird,book,bottle,bowl,broccoli,cake,car,cat,chair,clock,cow,cup,diningtable,dog,frisbee,handbag,horse,keyboard,knife,laptop,microwave,motorbike,mouse,orange,oven,person,refrigerator,remote,scissors,sink,sofa,spoon,suitcase,surfboard,tie,toothbrush,train,tvmonitor,umbrella,vase


