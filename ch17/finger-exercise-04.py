# Finger exercise: Find the area between -1 and 1 for a standard
# normal distribution.

import numpy as np
import scipy.integrate

def gaussian(x, mu, sigma):
    """Assumes x, mu, sigma are numbers
       Returns the value of P(x) for a Gaussian with mean mu and sd sigma
    """
    factor1 = (1.0 / (sigma*((2*np.pi)**0.5)))
    factor2 = np.e**-(((x-mu)**2)/(2*sigma**2))
    return (factor1 * factor2)

area = round(scipy.integrate.quad(gaussian, -1, 1, (0, 1))[0], 4)
print(f'Area = {area}')
