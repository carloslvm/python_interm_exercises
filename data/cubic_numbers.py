#!/usr/bin/python3

# Cubic numbers.
import matplotlib.pyplot as plt

x = list(range(50))
y = []
for get_y in x:
    y_value = y.append(get_y**3)

plt.scatter(x, y, s=40, c='r', edgecolor='none')
plt.title("Cubic Numbers", fontsize=24)
plt.xlabel("X Values", fontsize=14)
plt.ylabel("Y Values", fontsize=14)
plt.tick_params(axis='both', labelsize=10)

# Saving the plot
plt.savefig('plot_images/cubic_numbers.png',
        bbox_inches='tight')

plt.show()
