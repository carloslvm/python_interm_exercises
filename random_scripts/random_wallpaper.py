#!/usr/bin/python3

import random
import os 

# Path to my Wallpapers
wallpapers = "/home/carlos/Pictures/Wallpapers/"

# Saving Wallpaper in a list
images = os.listdir(wallpapers)

# Creating to the command for background
feh = "feh --bg-scale"

# Selecting a wallpaper randomly
select = random.choice(images)

# Changing the wallpaper
command = feh + " " + wallpapers + select
wallpaper_random = os.system(command )
