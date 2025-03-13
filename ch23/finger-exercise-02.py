# Finger exercise: Write an expression that selects all even
# numbered rows in wwc.

import pandas as pd

wwc = pd.read_csv('ch23/wwc2019_q-f.csv')
print(wwc.loc[::2]) # selects all even numbered rows