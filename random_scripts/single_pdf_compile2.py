#!/usr/bin/python3

# This script will work with all opened files in Vim
# that has the extension .tex

# This is an improved version of the first script.

import os

# Bash command to execute.
bash = "ls -a | grep swp | cut -d. -f2,3 | grep tex$ | xargs pdflatex"

# Compile the File.
os.system(bash)
