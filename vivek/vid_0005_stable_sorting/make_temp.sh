#!/bin/bash
set -x
BASE_PATH=/Users/vpandey/git/manim/media/videos
RES=$1

echo file $BASE_PATH/scenes/$RES/RadixSort.mp4      > mylist.txt

ffmpeg -y -f concat -safe 0 -i mylist.txt -c copy -f mp4 -vcodec h264 -pix_fmt yuv420p output.mov
ffmpeg -y -i output.mov -i audio-3.m4a -pix_fmt yuv420p output-with-audio.mov
open output-with-audio.mov
