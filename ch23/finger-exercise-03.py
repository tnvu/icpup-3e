# Finger exercise: Write an expression that generates the
# DataFrame
#      Round      Winner W Goals  Loser L Goals
# 1 Quarters         USA       2 France       1
# 2 Quarters Netherlands       2  Italy       0

import pandas as pd

wwc = pd.read_csv('ch23/wwc2019_q-f.csv')
print(wwc.loc[1:2])