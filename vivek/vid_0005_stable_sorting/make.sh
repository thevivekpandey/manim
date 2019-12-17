#!/bin/bash
set -x
BASE_PATH=/Users/vpandey/git/manim/media/videos
RES=$1

echo file $BASE_PATH/scenes/$RES/Opening.mp4        >  mylist.txt
echo file $BASE_PATH/scenes/$RES/ThreeQuestions.mp4 >> mylist.txt
echo file $BASE_PATH/scenes/$RES/SortingAlgos.mp4   >> mylist.txt
echo file $BASE_PATH/scenes/$RES/BigDeal.mp4        >> mylist.txt
echo file $BASE_PATH/scenes/$RES/Bag.mp4            >> mylist.txt
echo file $BASE_PATH/scenes/$RES/Marks.mp4          >> mylist.txt

#ffmpeg -y -i excel.mov -ss 00:00:00 -t 00:00:12 -async 1 excel-1.mov
#ffmpeg -y -i excel.mov -ss 00:00:32 -t 00:00:06 -async 1 excel-2.mov
#ffmpeg -y -i excel.mov -ss 00:00:38 -t 00:00:38 -async 1 excel-3.mov

#echo file excel-1.mov >> mylist.txt
#echo file excel-2.mov >> mylist.txt
#echo file excel-3.mov >> mylist.txt

#echo file $BASE_PATH/scenes/$RES/RadixSort.mp4      >> mylist.txt

#combine audios
echo file audio-1.m4a >  sound.txt
echo file audio-2.m4a >> sound.txt
ffmpeg -y -f concat -safe 0 -i sound.txt -c copy -f mp4 -vcodec h264 -pix_fmt yuv420p audio.m4a
ffmpeg -y -f concat -safe 0 -i mylist.txt -c copy -f mp4 -vcodec h264 -pix_fmt yuv420p output.mov
#ffmpeg -y -i output.mov -i speech-take-1.m4a -pix_fmt yuv420p output-with-audio.mov
ffmpeg -y -i output.mov -i audio.m4a -pix_fmt yuv420p output-with-audio.mov
