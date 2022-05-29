#!/usr/bin/python3

"""
This script is connected to vim_keys.py script. It allows
to show my personal Vim keybindings in a neatly format
using dmenu.

It requires to have dmenu installed on your Linux distro
to make it work.

Author: Carlos
"""
import os

# dmenu options
text_color = "\"#BD9842\" -sb "
selector = "\"#4F3600\" -sf "
f_selector = "\"#FFCD59\" -b -l 20"
prompt = "\"Vim Shortcuts\" -nf "
menu = "dmenu -p "

# Command Variable
dmenu = menu + prompt + text_color + selector + f_selector

# Printing Vim keybindings
vim_keybind = "python3 /home/carlos/.vim/vim_keys.py"

# Cleaning output (removing useless spaces)
space = " | sed '/^$/d' "

# Full Command
command = vim_keybind + space + "| "  + dmenu

# Run the Command
os.system(command)
