#!/usr/bin/env python3

from die import Die
import pygal

# Creating Dice
die_1 = Die(8)
die_2 = Die(8)

# Roll the dice
results = []
for result in range(5000000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze Results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Graph Representation
hist = pygal.Bar()

hist.title = " Rolling two D8 dice "
labels = []

for label in range(2, 17):
    lab_str = str(label)
    labels.append(lab_str)

hist.x_labels = labels
hist.x_title = " Results "

hist.y_title = " Frequencies "

hist.add('D8 + D8', frequencies)
hist.render_to_png('D8.png')

