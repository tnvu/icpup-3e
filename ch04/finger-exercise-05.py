# Finger exercise: Using the algorithm of Figure 3-6, write a
# function that satisfies the specification
# def log(x, base, epsilon):
#   """Assumes x and epsilon int or float, base an int,
#   x > 1, epsilon > 0 & power >= 1
#   Returns float y such that base**y is within epsilon
#   of x."""

def log(x, base, epsilon):
    """Assumes x and epsilon int or float, base an int,
    x > 1, epsilon > 0 & power >= 1
    Returns float y such that base**y is within epsilon
    of x."""
    lower_bound = 0
    while base**lower_bound < x:
        lower_bound += 1
    low = lower_bound - 1
    high = lower_bound + 1
    ans = (high + low) / 2
    while abs(base**ans - x) >= epsilon:
        if base**ans < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    return ans
