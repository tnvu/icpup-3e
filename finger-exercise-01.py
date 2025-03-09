# Finger exercise: An investigative reporter discovered that not only
# was Lyndsay employing dubious statistical methods, she was
# applying them to data she had merely made up. In fact, John had
# defeated Lyndsay 479 times and lost 443 times. At what level is this
# difference statistically significant?

import random
import scipy

john_wins = 479
john_losses = 443
num_games = john_wins + john_losses
outcomes = [1.0]*john_wins + [0.0]*john_losses
print('The p-value from a one-sample test is',
      scipy.stats.ttest_1samp(outcomes, 0.5)[1])


num_trials = 10000
at_least = 0
for t in range(num_trials):
    j_wins, j_losses = 0, 0
    for g in range(num_games):
        if random.random() < 0.5:
            j_wins += 1
        else:
            j_losses += 1
    if j_wins >= john_wins or j_losses >= john_wins:
        at_least += 1
print('Probability of results at least this extreme by accident = ',
      at_least/num_trials)
