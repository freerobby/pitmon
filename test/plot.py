#!/usr/bin/env python2.7

import json
import matplotlib.pyplot as plt
import config

statefile = open(config.output)
readings = json.load(statefile)
x = []
y1 = []
y2 = []
y2 = []
y3 = []
y4 = []
l = []
t = []

idx = 0
tick = 0
for reading in readings:
    x.append(idx)
    y1.append(reading['COOK_TEMP'])
    y2.append(reading['FOOD1_TEMP'])
    y3.append(reading['FOOD2_TEMP'])
    y4.append(reading['FOOD3_TEMP'])
    if idx % 5 == 0:
        t.append(idx)
        l.append(reading['TIME'][:5])
        tick += 1
    idx += 1

plt.plot(x, y1, "rs", x, y2, "b^", x, y3, "gp", x, y4, "mD")
plt.ylabel('Temperature F')
plt.xticks(t, l)
plt.show()
