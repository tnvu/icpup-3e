# Finger exercise: Modify the code in Figure 20-5 so that it produces
# the plot in Figure 20-8.

import numpy as np
import matplotlib.pyplot as plt

def get_data(input_file):
    with open(input_file, 'r') as data_file:
        distances = []
        masses = []
        data_file.readline() # ignore header
        for line in data_file:
            d, m = line.split(',')
            distances.append(float(d))
            masses.append(float(m))
    return (masses, distances)  # why flip order of distances and masses?

def fit_data(input_file):
    masses, distances = get_data(input_file)
    forces = np.array(masses) * 9.81
    plt.plot(forces, distances, 'ko', label = 'Measured displacements')
    plt.title('Measured Displacement of Spring')
    plt.xlabel('|Force| (Newtons)')
    plt.xticks(np.arange(0, 16, step=5))
    plt.ylabel('Distance (meters)')
    plt.yticks(np.arange(-0.50, 0.76, step=0.25))
    predicted_forces = np.array(masses + [1.5]) * 9.81
    # Find linear fit
    a, b = np.polyfit(forces, distances, 1)
    predicted_distances = a * np.array(predicted_forces) + b
    k = 1.0 / a # see explanation in text
    plt.plot(predicted_forces, predicted_distances, label = f'Linear fit, k = {k:.4f}')
    # Find cubic fit
    fit = np.polyfit(forces, distances, 3)
    predicted_distances = np.polyval(fit, predicted_forces)
    plt.plot(predicted_forces, predicted_distances, 'k:', label = 'Cubic fit')
    
    plt.legend(loc = 'best')

fit_data('./ch20/springData.csv')
