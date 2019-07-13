#!/usr/bin/python3

import matplotlib.pyplot as plt

# X Values
x = [-2, -1, 0, 1, 2]

# Y Values
y = [2, 1, 0, 1, 2]

plt.plot(x, y, linewidth=2)
plt.title("Absolute Value Function", fontsize=24)
plt.xlabel("X Values", fontsize=10)
plt.ylabel("Y Values", fontsize=10)
plt.tick_params(axis='both', labelsize=14)

plt.show()
