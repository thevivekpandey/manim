#!/bin/bash
BASE_PATH=/Users/vpandey/git/manim/vivek/vid_0003_selection_sort/videos
RES=$1
ffmpeg -y -i $BASE_PATH/scenes/$RES/Opening.mp4   -ss 00:00:00 -t 00:00:03 -async 1 edited-slide-00.mov
ffmpeg -y -i $BASE_PATH/scenes/$RES/Topic.mp4     -ss 00:00:00 -t 00:00:09 -async 1 edited-slide-01.mov #00:12
ffmpeg -y -i $BASE_PATH/scenes/$RES/RealWorld.mp4 -ss 00:00:00 -t 00:00:16 -async 1 edited-slide-02.mov #00:28
ffmpeg -y -i $BASE_PATH/children/$RES/Children.mp4  -ss 00:00:00 -t 00:02:04 -async 1 edited-slide-03.mov #02:32
ffmpeg -y -i $BASE_PATH/algorithm/$RES/Algorithm.mp4 -ss 00:00:00 -t 00:05:00 -async 1 edited-slide-04.mov #

echo file edited-slide-00.mov >  mylist.txt
echo file edited-slide-01.mov >> mylist.txt
echo file edited-slide-02.mov >> mylist.txt
echo file edited-slide-03.mov >> mylist.txt
echo file edited-slide-04.mov >> mylist.txt

ffmpeg -y -f concat -i mylist.txt -c copy -f mp4 -vcodec h264 -pix_fmt yuv420p output.mov
ffmpeg -y -i output.mov -i output.m4a -pix_fmt yuv420p output-with-audio.mov
