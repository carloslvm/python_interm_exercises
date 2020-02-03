#!/usr/bin/env python3

from die import Die
import pygal

# Creating Dice
die1 = Die()
die2 = Die()
die3 = Die()

# Rolling the dice
results = []

for roll_num in range(300000):
    result = die1.roll() + die2.roll() + die3.roll()
    results.append(result)


# Analyze results
frequencies = []
max_results = die1.num_sides + die2.num_sides + die3.num_sides

for value in range(3, max_results+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize Results
hist = pygal.Bar()
hist.title = " Rolling Three Dice "

labels = []
for label in range(3, 19):
    lab_con = str(label)
    labels.append(label)

hist.x_labels = labels
hist.x_title = "Results"
hist.y_title = "Frequency"

hist.add('D6 + D6 + D6', frequencies)

hist.render_to_png('three_dice.png')
