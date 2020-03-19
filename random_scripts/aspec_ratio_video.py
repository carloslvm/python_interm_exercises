#!/usr/bin/python3

import os

"""
This script changes the aspect ratio of a video
using ffmpeg.

Make sure you have ffmpeg installed and run this
script on Linux enviroment.
""" 
# Video Sources
videos = os.listdir()

#video_formats = ['.webm', '.mkv', '.flv', '.vob',
#        '.ogg', '.ogv', '.avi', '.mov', 'wmv',
#        '.mp4', '.flv']

videos_target = []
for video in videos:
    if '.mp4' in video:
        print(videos.index(video), video)
        videos_target.append("\"" + video + "\"")

# Selecting aspect ratio
aspect_ratio = input("Enter the output aspect ratio: ")

# Command creation
command_1 = "ffmpeg -i "
command_2 = "-aspect " + aspect_ratio + " -qscale 0 "

format_command_1 = []

for input_video in videos_target:
    if '.mp4' in input_video:
        ffmpeg_1 = command_1 + input_video
        #print(ffmpeg_1)
        format_command_1.append(ffmpeg_1)

format_command_2 = []

for output_video in videos_target:
    if '.mp4' in output_video:
        #for output in range(len(videos)):
        indexes = videos_target.index(output_video)
        ffmpeg_2 = command_2 + " " + str(indexes) + output_video
        #print(ffmpeg_2)
        format_command_2.append(ffmpeg_2)

complete_command = []

for c_command in range(len(format_command_1)):
    complete = format_command_1[c_command] + " " + format_command_2[c_command]
    print(complete)
    complete_command.append(complete)

# Executing command
#for execute in complete_command:
#    os.system(execute)
print("Conversion completed.")
