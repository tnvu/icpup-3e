# Finger exercise: Write an expression that computes the total
# number of goals scored by the losing teams in the quarter finals.

import pandas as pd

wwc = pd.read_csv('ch23/wwc2019_q-f.csv')
print('Total goals by losing teams in quarter finals: ',
      wwc[wwc['Round'] == 'Quarters']['L Goals'].sum())