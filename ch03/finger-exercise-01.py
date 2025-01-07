# Finger exercise: Change the code in Figure 3-2 so that it returns
# the largest rather than the smallest divisor. Hint: if y*z = x and y is
# the smallest divisor of x, z is the largest divisor of x.

# Test if an int > 2 is prime. If not, print largest divisor
x = int(input('Enter an integer greater than 2: '))
largest_divisor = None
for guess in range(2, x):
    if x % guess == 0:
        largest_divisor = x // guess
        break
if largest_divisor != None:
    print(f'Largest divisor of {x} is {largest_divisor}')
else:
    print(f'{x} is a prime number')
