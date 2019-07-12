#!/usr/bin/python3

# Basic Exponential Function plot.

import matplotlib.pyplot as plt

#X values
x_values = [-3, -2, -1, 0, 1, 2, 3, 4]

#Y values
y_values = [8, 4, 2, 1, 1/2, 1/4, 1/8, 1/16]

plt.plot(x_values, y_values, linewidth=2)

plt.title("Exponential Function", fontsize=20)

plt.xlabel("X Value", fontsize=10)
plt.ylabel("Y Value", fontsize=10)

plt.tick_params(axis='both', labelsize=14)

plt.show()
