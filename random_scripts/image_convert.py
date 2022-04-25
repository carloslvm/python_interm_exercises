#!/usr/bin/python3

import os

"""
This is a test script. It should convert a massive amount
of images located in a specific directory to any format
the user wants.

This script was tested on Linux, it is necessary to have
ImageMagick package installed to run it properly.

Author: Carlos
"""

# Input Directory (input images container)

images_path = input("Enter directory path: ")
images_input = os.listdir(images_path)

# Selecting Input Format

image_input_format = input("Enter input format: ")

# Creating Command (First Part)

command_1 = []

for image_input in images_input:
    if image_input_format in image_input:
        format_input = "convert " + "\"" + image_input +"\""
        command_1.append(format_input)
        

# Selecting output format

image_output_format = input("Enter output format: ")

# Creating Command (Second part)

output_image = []

for output in images_input:
    if image_input_format in output:
        result = "\"" + output.replace(image_input_format, image_output_format) + "\""
        output_image.append(result)


# Full command
complete_command = []

for full_command in range(len(command_1)):
    complete = command_1[full_command] + " " + output_image[full_command]
    print(complete)
    complete_command.append(complete)

# Conversion 
for conversion in complete_command:
    os.system(conversion)

# Creating a new directory
result = os.system("mkdir -v result")

# Send converted images to result
images_result = os.listdir()

for send in images_result:
    if ".jpg" in send:
        print(send)
        sending = "mv -v " + "\"" + send + "\"" + " result/"
        os.system(sending)
