# Finger exercise: Write a function that returns the sum of the goals
# scored by winners.

import pandas as pd

def sum_w_goals(df):
    goals = 0
    for g in df['W Goals']:
        goals += g
    return goals

wwc = pd.read_csv('ch23/wwc2019_q-f.csv')
print("Winner goals = ", sum_w_goals(wwc))