#!/usr/bin/python3

import os

"""
This script was created to transcode videos files.
Make sure you have ffmpeg installed and run this
script on Linux.


Author: Carlos
"""

# Videos to transcode.
videos = os.listdir()

format_input = input("Enter the input format: ")
for video in videos:
    if format_input in video:
        print(video)

# Selecting the video format.
formatting = input("Enter the output format: ")

# Format preview.
new_videos = []
for output_preview in videos:
    if format_input in output_preview:
        preview = output_preview.replace(format_input, formatting)
        print(preview)
        new_videos.append(preview) 

# Format confirmation.
confirm = input("Continue? (y/n): ")

# Command creation.
command_1 = "ffmpeg -i "
#command_2 = "-qscale 0 "
command_2 = "-c:v copy -c:a copy " # Faster conversion, not recommended for avi

format_command_1 = []

for video_source in videos:
    if format_input in video_source:
        ffmpeg_1 = command_1 + "\"" + video_source + "\""
        #print(ffmpeg_1)
        format_command_1.append(ffmpeg_1)

format_command_2 = []

for video_output in new_videos:
    ffmpeg_2 = command_2 + "\"" + video_output + "\""
    #print(ffmpeg_2)
    format_command_2.append(ffmpeg_2)


complete_command = []

for c_command in range(len(format_command_1)):
    complete = format_command_1[c_command] + " " + format_command_2[c_command]
    #print(complete)
    complete_command.append(complete)

# Creating output directory
result = "mkdir result" 
os.system(result)

# Conversion
if confirm == "y":
    for conversion in complete_command:
        os.system(conversion)
    print("Conversions completed.")
elif confirm == "n":
    print("Operation aborted.")
else:
    print("Unknown command.")

# Sending output videos to result directory
move_command = "mv -v *" + formatting + " result/"
os.system(move_command)


# Automatic video converter edited successfully.
# Issue solved: Name of input videos with spaces and output
#               videos with spaces.
# Solution: Putting input videos and output videos in double quotes.

# Faster conversion added.
# Send output to a new directory.
