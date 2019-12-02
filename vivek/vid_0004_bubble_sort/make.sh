#!/bin/bash
set -x
BASE_PATH=/Users/vpandey/git/manim/vivek/vid_0004_bubble_sort/videos
RES=$1

echo file $BASE_PATH/scenes/$RES/Opening.mp4               > mylist.txt
echo file $BASE_PATH/scenes/$RES/LastVideo.mp4            >> mylist.txt
echo file $BASE_PATH/scenes/$RES/IntroduceBubbleSort.mp4  >> mylist.txt
echo file $BASE_PATH/bubbles/$RES/Bubbles.mp4             >> mylist.txt
echo file $BASE_PATH/scenes/$RES/Knuth.mp4                >> mylist.txt
echo file $BASE_PATH/scenes/$RES/WhySlow.mp4              >> mylist.txt
echo file $BASE_PATH/scenes/$RES/Nature.mp4               >> mylist.txt
echo file $BASE_PATH/bubbles1/$RES/Bubbles.mp4            >> mylist.txt
echo file $BASE_PATH/scenes/$RES/Improvement.mp4          >> mylist.txt
echo file $BASE_PATH/scenes/$RES/Manindra.mp4             >> mylist.txt

ffmpeg -y -f concat -safe 0 -i mylist.txt -c copy -f mp4 -vcodec h264 -pix_fmt yuv420p output.mov
ffmpeg -y -i output.mov -i output.m4a -pix_fmt yuv420p output-with-audio.mov
