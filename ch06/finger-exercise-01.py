# Finger exercise: The harmonic sum of an integer, n > 0, can be
# calculated using the formula . Write a recursive function
# that computes this.

def harmonic_sum(n):
    """Returns the harmonic sum of an integer n > 0."""
    if n == 1:
        return n
    else:
        return harmonic_sum(n-1) + 1/n