# Finger exercise: Add some code to the implementation of
# Newton–Raphson that keeps track of the number of iterations used
# to find the root. Use that code as part of a program that compares the
# efficiency of Newton–Raphson and bisection search. (You should
# discover that Newton–Raphson is far more efficient.)

k = 24
# Newton-Raphson for square root
epsilon = 0.01
guess = k / 2
num_guesses = 0
while abs(guess**2 - k) >= epsilon:
    guess = guess - ((guess**2 - k) / (2 * guess))
    num_guesses += 1
print(f'Square root of {k} is about {guess} ({num_guesses} guesses)')
