# Finger exercise: Use the tabular method to implement a dynamic
# programming solution that meets the specification
#   def make_change(coin_vals, change):
#       """coin_vals is a list of positive ints and coin_vals[0] = 1
#          change is a positive int,
#          return the minimum number of coins needed to have a set of
#          coins the values of which sum to change. Coins maybe used
#          more than once. For example,
#          make_change([1, 5, 8], 11) should return 3."""

def make_change(coin_vals, change):
    """coin_vals is a list of positive ints and coin_vals[0] = 1
       change is a positive int,
       return the minimum number of coins needed to have a set of coins the
       values of which sum to change. Coins maybe used more than once.
       For example, make_change([1, 5, 8], 11) should return 3."""
    coin_vals = sorted(coin_vals)
    tab = [0] * (change+1)
    for value in range(change+1):
        for j in range(len(coin_vals)-1):
            coin = coin_vals[j]
            next_coin = coin_vals[j+1]
            if value < coin or value == next_coin:
                continue
            tab[value] = 1 + tab[value-coin]
    return tab[change]
