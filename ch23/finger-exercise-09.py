# Finger exercise: Write code to extract the date on which the
# temperature in Phoenix was 41.4C.

import pandas as pd

temperatures = pd.read_csv('ch23/US_temperatures.csv')
temperatures.loc[(temperatures['Phoenix']==41.4)]['Date']