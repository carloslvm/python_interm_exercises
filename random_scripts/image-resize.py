#!/usr/bin/python3

import os

"""
Script for resizing a massive amount of images using
ImageMagick commands. Make sure you have ImageMagick
installed on your system.

This script was tested on Linux system only.

Author: Carlos
"""

# Images available in directory
images = os.listdir()

# Select image input format
format_input = input("Enter input format: ")

# Listing input and output images
image_in_out = []
for image in images:
    if format_input in image:
        inp_out = image + " XYZ-" + image
        print(inp_out)
        image_in_out.append(inp_out)

# Dimensions in pixels
dimensions = input("Dimensions? (example: 1024x768): ")

# ImageMagick command 
command = "convert -resize " + dimensions

# Command preview
full_command = []
for preview_command in image_in_out:
    complete_command = command + " " + preview_command
    print(complete_command)
    full_command.append(complete_command)

# Creating output directory
os.system("mkdir output")

# Move command
move = "mv XYZ-* output/"

# Resizing images
for execute in full_command:
    print("Resizing: " + execute)
    os.system(execute)

# Updating directory's content
update_image_list = os.listdir()

# Sending images to output directory
for moving in update_image_list:
    if "XYZ-" in moving:
        os.system(move)

"""
Issues to solve:
    Name of files must not have spaces or 
    special characters.

    Script works but there's an error message at the
    end of the execution (directory not found)
"""
