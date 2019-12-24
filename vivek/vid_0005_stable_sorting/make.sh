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

#ffmpeg -y -i excel.mov -ss 00:00:08 -t 00:01:13 -async 1 excel-cut.mov
echo file excel-cut.mov >> mylist.txt

echo file $BASE_PATH/scenes/$RES/RadixSort.mp4      >> mylist.txt
echo file $BASE_PATH/scenes/$RES/StableAlgos.mp4    >> mylist.txt
echo file $BASE_PATH/scenes/$RES/AnotherWay.mp4     >> mylist.txt
echo file $BASE_PATH/scenes/$RES/GoodBye.mp4        >> mylist.txt

#combine audios
#echo file audio-1.m4a     >  sound.txt
#echo file audio-2-3-4.m4a >> sound.txt
#echo file audio-5.m4a     >> sound.txt
#echo file audio-6.m4a     >> sound.txt
#echo file audio-7.m4a     >> sound.txt
#echo file audio-8.m4a     >> sound.txt
#ffmpeg -y -f concat -safe 0 -i sound.txt -c copy -f mp4 -vcodec h264 -pix_fmt yuv420p audio.m4a

ffmpeg -y -f concat -safe 0 -i mylist.txt -c copy -f mp4 -vcodec h264 -pix_fmt yuv420p output.mov
ffmpeg -y -i output.mov -i audio.m4a -pix_fmt yuv420p output-with-audio.mov
open output-with-audio.mov
