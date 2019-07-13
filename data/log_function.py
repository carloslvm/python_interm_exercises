#!/usr/bin/python3

import matplotlib.pyplot as plt

# X Values
x = [1/6, 1/8, 1/4, 1/2, 1, 2, 4, 8, 16]

# Y Values
y = [-4, -3, -2, -1, 0, 1, 2, 3, 4]

plt.plot(x, y, linewidth=2)

plt.title("Logarithmic Function", fontsize=14)

plt.xlabel("X Value", fontsize=12)
plt.ylabel("Y Value", fontsize=12)

plt.tick_params(axis='both', labelsize=14)

plt.show()
