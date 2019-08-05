#!/usr/bin/python3

# Negative cubic numbers

import matplotlib.pyplot as plt

x = list(range(-50,12))
y = []

for get_y in x:
    y_value = y.append(get_y**3)

plt.scatter(x, y, s=40, edgecolor='none', c='purple')
plt.title("Negative Cubic Numbers", fontsize=24)
plt.xlabel("X Values", fontsize=14)
plt.ylabel("Y Values", fontsize=14)
plt.tick_params(axis='both', labelsize=10)

# Saving the image
plt.savefig('plot_images/negCubic_numbers.png',
        bbox_inches='tight')

plt.show()
