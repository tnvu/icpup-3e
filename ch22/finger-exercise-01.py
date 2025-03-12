# Finger exercise: It is sometimes illuminating to plot things relative
# to a baseline, as seen in Figure 22-4. Modify plot_housing to produce
# such plots. The bars below the baseline should be in red. Hint: use
# the bottom keyword argument to plt.bar.

import matplotlib.pyplot as plt
import numpy as np

def plot_housing(impression):
    """Assumes impression a str. Must be one of 'flat', 'volatile', and 'fair'
       Produce a bar chart of housing prices over time
    """
    labels, prices, colors = [], [], []
    baseline = 200
    with open('./ch22/midWestHousingPrices.csv', 'r') as f:
        # Each line of file contains year, quarter, price
        # for Midwest region of U.S.
        for line in f:
            year, quarter, price = line.split(',')
            label = year[2:4] + '\n Q' + quarter[1]
            labels.append(label)
            price = int(price)/1000 - baseline
            prices.append(price)
            if price >= 0:
                colors.append('blue')
            else:
                colors.append('red')
    quarters = np.arange(len(labels)) # x-coords of bars
    width = 0.8 # width of bars
    plt.bar(quarters, prices, width, bottom=baseline, color=colors)
    plt.xticks(quarters + width/2, labels)
    plt.title('Housing Prices in U.S. Midwest')
    plt.xlabel('Quarter')
    plt.ylabel('Average Price ($1,000\'s)')
    if impression == 'flat':
        plt.ylim(1, 500)
    elif impression == 'volatile':
        plt.ylim(180, 220)
    elif impression == 'fair':
        plt.ylim(150, 250)
    else:
        raise ValueError

plot_housing('flat')
plt.figure()
plot_housing('volatile')
plt.figure()
plot_housing('fair')
plt.figure()