# Finger exercise: Use the find_root function in Figure 4-3 to print
# the sum of approximations to the square root of 25, the cube root of
# -8, and the fourth root of 16. Use 0.001 as epsilon.

# Figure 4-3
def find_root(x, power, epsilon):
    if x < 0 and power % 2 == 0:
        return None # Negative number has no even powered roots
    low = min(-1, x)
    high = max(1, x)
    ans = (high + low) / 2
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    return ans

epsilon = 0.01
print(find_root(25, 2, epsilon) + 
      find_root(-8, 3, epsilon) + 
      find_root(16, 4, epsilon))