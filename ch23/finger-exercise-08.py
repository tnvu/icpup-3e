# Finger exercise: Write an expression that evaluates to True if
# Phoenix was warmer than Tampa on October 31, 2000, and False
# otherwise.

import pandas as pd

temperatures = pd.read_csv('ch23/US_temperatures.csv')
temperatures.loc[temperatures['Date']==20001031]['Phoenix'] > \
    temperatures.loc[temperatures['Date']==20001031]['Tampa']