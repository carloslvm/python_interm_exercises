#!/usr/bin/python3

# This script only works with one opened file.

import os

# Compile the current opened file.
command = os.system("ls -a | grep swp | cut -d. -f2,3 | grep$ | xargs pdflatex")

try:
    os.system(command)
except TypeError:
    pass
    #print("Compilation completed")
