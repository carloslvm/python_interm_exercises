#!/usr/bin/python3

from random import choice

class RandomWalk():
    """ Random walk generator."""

    def __init__(self, points=2000):
        self.points = points

        self.x_values = [0] #Mutable Variable
        self.y_values = [0] #Mutable Variable

    def x_walk(self):
        """X Steps"""
        x_direction = choice([1, -1])
        x_distance = choice(list(range(-100, 101)))
        return x_direction * x_distance

    def y_walk(self):
        """Y Steps"""
        y_direction = choice([1, -1])
        y_distance = choice(list(range(-100, 101)))
        return y_direction * y_distance

    def walk(self):
        """Starting the walk."""
        while len(self.x_values) < self.points:

            x_step = self.x_walk()
            y_step = self.y_walk()

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
