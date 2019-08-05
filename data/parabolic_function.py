#!/usr/bin/python3

import matplotlib.pyplot as plt

x = range(10, -10)

y = []
for variable in x:
    operation = (variable**2) - 4*variable + 3
    s = y.append(operation)

plt.plot(figsize=(10, 6))
plt.plot(x, y, linewidth=2)
#plt.plot(x2, y2, linewidth=2)
plt.title("Parabolic Function", fontsize=24)
plt.xlabel("X Values", fontsize=10)
plt.ylabel("Y Values", fontsize=10)
plt.tick_params(axis='both', labelsize=14)
plt.show()
