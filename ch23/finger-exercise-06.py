# Finger exercise: Write an expression that computes the total
# number of goals scored in all of the rounds.

import pandas as pd

wwc = pd.read_csv('ch23/wwc2019_q-f.csv')
print('Total number of goals:', wwc['W Goals'].sum() + wwc['L Goals'].sum())
