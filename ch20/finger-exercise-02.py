# Finger exercise: In a vacuum, the speed of a falling object is
# defined by the equation v = v0 + gt, where v0 is the initial velocity of
# the object, t is the number of seconds the object has been falling, and
# g is the gravitational constant, roughly 9.8 m/sec**2 on the surface of
# the Earth and 3.711 m/sec**2 on Mars. A scientist measures the
# velocity of a falling object on an unknown planet. She does this by
# measuring the downward velocity of an object at different points in
# time. At time 0, the object has an unknown velocity of v0. Implement
# a function that fits a model to the time and velocity data and
# estimates g for that planet and v0 for the experiment. It should
# return its estimates for g and v0, and also r-squared for the model.

import numpy as np

def r_squared(measured, predicted):
    """Assumes measured a one-dimensional array of measured values
               prediced a one-dimensional array of predicted values
       Returns coefficients of determination
    """
    estimated_error = ((predicted - measured)**2).sum()
    mean_of_measured = measured.sum() / len(measured)
    variability = ((measured - mean_of_measured)**2).sum()
    return 1 - (estimated_error / variability)

def estimate_g(velocity_data, time_data):
    # v(t) = gt
    fit = np.polyfit(time_data, velocity_data, 1)
    g = fit[0]
    v0 = np.polyval(np.poly1d(fit), 0)
    r2 = r_squared(velocity_data, np.polyval(fit, time_data))    
    return (g, v0, r2)
