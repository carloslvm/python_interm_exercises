#!/usr/bin/env python3

from die import Die
import pygal

# Instances Dice
die1 = Die()
die2 = Die()

# Rolling
results = []

for result in range(200000):
    result = die1.roll() * die2.roll()
    results.append(result)

# Analyzing
freqs = []
max_results = die1.num_sides * die2.num_sides

for value in range(4, max_results+1):
    freq = results.count(value)
    freqs.append(freq)

# Visualization
hist = pygal.Bar()
hist.title = "Multiply Dice"

labels = []
for label in range(2, 36):
    lab_con = str(label)
    labels.append(label)

hist.x_labels = labels
hist.x_title = "Results"
hist.y_title = "Frequency"

hist.add("D6 * D6", freqs)
hist.render_to_png("multiply.png")

