#!/usr/bin/python3

"""
This script reads my personal vimrc file and filter my
custom keybindings. As preference, I put this script
in the same directory where the vimrc file is located.

If you want to save this in a different directory, make
sure to edit the path in the source code of this script
and vim_shortcuts.py script.

Author: Carlos
"""
# File to read
vimrc = '/home/carlos/.vim/vimrc'

# Reading and creating a list of each line in vimrc.
with open(vimrc, 'r') as vim:
    vim_shortcuts = vim.readlines()

# Printing the selected lines from the previous list.
for key in vim_shortcuts[58:]:
    print(key)
