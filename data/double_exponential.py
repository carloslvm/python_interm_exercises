#!/usr/bin/python3

# y = (1/2)**x      y = 2**x

import matplotlib.pyplot as plt

exponent = 5 #X

x = list(range(-5, exponent + 1))

y = []
y2 = []

for y_value in range(-5, exponent + 1):
    get_y = y.append(2**y_value)
    get_y2 = y2.append((1/2)**y_value)


plt.plot(x, y, linewidth=2, label='Curve 1')
plt.plot(x, y2, linewidth=2, label='Curve 2')

plt.title("Exponential Curves", fontsize=24)
plt.xlabel("X Value", fontsize=10)
plt.ylabel("Y Value", fontsize=10)

plt.tick_params(axis='both', labelsize=14)

# Show the legend of the plot.
plt.legend()

plt.show()

