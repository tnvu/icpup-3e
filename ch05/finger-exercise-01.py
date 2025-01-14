# Finger exercise: Write an expression that evaluates to the mean of
# a tuple of numbers. Use the function sum.

def mean(numbers):
    return 0 if len(numbers) == 0 else sum(numbers) / len(numbers)
