#!/usr/bin/python3

# Cubic Function with colormap and scatter.

import matplotlib.pyplot as plt

x = list(range(-2000, 2001))
y = []
for x_pow in x:
	y_value = y.append(x_pow**3)

plt.scatter(x, y, s=40, c=y , cmap=plt.cm.Reds,
		edgecolor='none')
plt.title("Colormap Cubic Function", fontsize=24)
plt.xlabel("X Values", fontsize=12)
plt.ylabel("Y Values", fontsize=12)
plt.tick_params(axis='both', labelsize=10)

# Saving the image
directory = 'plot_images/'
save_file = directory + 'colormap_cubic_function.png'
plt.savefig(save_file, bbox_inches='tight')

plt.show()
