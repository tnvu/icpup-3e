# Finger exercise: Write an expression that returns a DataFrame
# containing games in which the USA but not France played.

import pandas as pd

wwc = pd.read_csv('ch23/wwc2019_q-f.csv')
print(wwc.loc[
    ((wwc['Winner'] == 'USA') & (wwc['Loser'] != 'France')) |
    ((wwc['Winner'] != 'France') & (wwc['Loser'] == 'USA'))])
