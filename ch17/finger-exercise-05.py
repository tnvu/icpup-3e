# Finger exercise: Use the above formula to implement a function
# that calculates the probability of rolling exactly two 3’s in k rolls of a
# fair die. Use this function to plot the probability as k varies from 2 to
# 100.

import math
import matplotlib.pyplot as plt

def probability_of_two_threes(num_rolls):
    return math.comb(num_rolls, 2) * (1/6)**2 * (1 - 1/6)**(num_rolls-2)

xAxis = []
yAxis = []
for x in range(2, 100+1):
    xAxis.append(x)
    yAxis.append(probability_of_two_threes(x))
plt.plot(xAxis, yAxis, 'k')