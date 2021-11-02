#!/usr/bin/python3

#import re
import os

"""
This script was created to compile tex files
from Vim text editor. Remember to put it in
/usr/bin/ directory.
"""

# Storing directoy's content in a list.
directory_content = os.listdir()

# Printing only tex file to compile.
for tex_file in directory_content:
    if "tex" in tex_file:
        print(directory_content.index(tex_file), tex_file)

# Selecting the file to compile.
tex_selection = int(input('Enter the index of the file: '))

tex_compile = directory_content[tex_selection]
print('File Selected:', tex_compile)

# Compiling the selected file.
pdf_command = 'pdflatex {0}'.format(tex_compile)

os.system(pdf_command)

# Issue to solve: discriminate 

# Issue to solve: discriminate any file that does not end
#                 with .tex extension.
# Possible solution: Try using python3 regex
