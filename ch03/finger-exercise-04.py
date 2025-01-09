# Finger exercise: What would the code in Figure 3-5 do if x = -25?

# Figure 3-5
x = -25
epsilon = 0.01
num_guesses, low = 0, 0
high = max(1, x)
ans = (high + low) / 2
while abs(ans**2 - x) >= epsilon:
    print(f'low={low}, high={high}, ans={ans}')
    num_guesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2
print(f'number of guesses={num_guesses}')
print(f'{ans} is close to the square root of {x}')

# if x = -25, the program would run forever
# low=0, high=1, ans=0.5
# low=0, high=0.5, ans=0.25
# low=0, high=0.25, ans=0.125
# ...