#!/usr/bin/python3

from random_walks import RandomWalk
import matplotlib.pyplot as plt

points = int(input('Enter the numer of points to plot: '))

active = True
while active:
    rw = RandomWalk(points)
    rw.x_walk()
    print("X data: " + repr(rw.x_walk()))
    rw.y_walk()
    print("Y data: " + repr(rw.y_walk()))
    rw.walk()

    plt.figure(figsize=(10, 6))

    points_number = list(range(rw.points))
    for point_number in points_number:
        print("Plotting Point: " + repr(point_number))

    plt.scatter(rw.x_values, rw.y_values, #cmap=plt.cm.Blues,
            c=points_number, #edgecolor='none',
            s=10)
    
    # Beginning point
    plt.scatter(0, 0, c='green', edgecolor='none',
            s=100)
    
    # Ending point
    plt.scatter(rw.x_values[-1], rw.y_values[-1],
            c='red', edgecolor='none', s=100)

    # Removing axes points
    plt.axes().get_xaxis().set_visible(True)
    plt.axes().get_yaxis().set_visible(True)

    plt.show()

    keep_plotting = input("Make another plot? (y/n): ")
    if keep_plotting == 'n':
        active = False
