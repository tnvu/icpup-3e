# Finger exercise: What would have to be changed to make the code
# in Figure 3-5 work for finding an approximation to the cube root of
# both negative and positive numbers? Hint: think about changing low
# to ensure that the answer lies within the region being searched.

x = 0.5

epsilon = 0.01
num_guesses, low = 0, 0
high = max(1, abs(x))
ans = (high + low) / 2
while abs(ans**3 - abs(x)) >= epsilon:
    print(f'low={low}, high={high}, ans={ans}')
    num_guesses += 1
    if ans**3 < abs(x):
        low = ans
    else:
        high = ans
    ans = (high + low) / 2
if x < 0:
    ans = -ans
print(f'number of guesses={num_guesses}')
print(f'{ans} is close to the cube root of {x}')
