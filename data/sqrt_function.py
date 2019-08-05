#!/usr/bin/python3

# Square root function (Scatter)

from math import sqrt
import matplotlib.pyplot as plt

x = list(range(20+1))

y = []
for get_y in x:
    y_values = y.append(sqrt(get_y))

plt.scatter(x, y, s=40, c='r', edgecolor='none')
plt.title("Square Root Function", fontsize=24)
plt.xlabel("X Values", fontsize=14)
plt.ylabel("Y Values", fontsize=14)

plt.tick_params(axis='both', labelsize=14)

# Setting up the path to save the plot as png.
path = '/home/carlos/REPOS/python_interm_exercises/data/plot_images/'
image = "Scatter: Square Root Function.png"
file_save = path + image

# Saving the image.
plt.savefig(file_save, bbox_inches='tight')
plt.show()
