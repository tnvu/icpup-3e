# Finger exercise: Print a DataFrame containing only the games in
# which Sweden played either Germany or Netherlands.

import pandas as pd

def get_games(df, countries):
    return df[df['Winner'].isin(countries) | df['Loser'].isin(countries)]

wwc = pd.read_csv('ch23/wwc2019_q-f.csv')
print(get_games(get_games(wwc, ['Sweden']), ['Germany', 'Netherlands']))