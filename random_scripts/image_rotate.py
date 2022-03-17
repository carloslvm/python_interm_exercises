#!/usr/bin/python3

import os

"""
This script rotates a massive amount of images 
usig ImageMagick. Make sure you have ImageMagick
installed on your system.

Tested on Linux only.


Author: Carlos
"""

# List of Images
images = os.listdir()

image_input = []
image_format = input("Enter image format: ")
for image in images:
    if image_format in image:
        print(image)
        image_input.append(image)

# Degree Selection
degree = int(input("How many degrees do you want to rotate: "))

# Preview name
new_images = []
for name_preview in image_input:
    if image_format in name_preview:
        preview = name_preview + " ROT-" + name_preview
        print(preview)
        new_images.append(preview)

# Command to rotate image
convert_rotate = "convert -rotate "

# New Directory
os.system("mkdir rotation")

# Command to move results to rotation
move = "mv ROT* rotation"

# Building Full Command
command_full = []
for command_input in new_images:
    command_1 = convert_rotate + str(degree) + " " + command_input
    print(command_1)
    command_piece1.append(command_1)

# Rotating Images
for execute in command_full:
    os.system(execute)

# Moving aoutput to rotation directory
images2 = os.listdir()

image_output = []
for image2 in images2:
    if "ROT-" in image2:
        print(image2)
        image_output.append(image2)

for move_output in image_output:
    os.system(move)


"""
Issues to solve:
    naming convention (names must not have spaces and
    special characters)

    Script works but there's an error message at the
    end of the execution (directory not found)
"""

