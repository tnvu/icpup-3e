# Finger exercise: When the implementation of fib in Figure 6-3 is
# used to compute fib(5), how many times does it compute the value
# of fib(2) on the way to computing fib(5)?

# Figure 6-3
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)
    
# for fib(5), fib(2) is calculated:
# n = 5 --> fib(3) + fib(4) --> 1 + (1 + 1)
# n = 4 --> fib(2) + fib(3) --> 1 + 1
# n = 3 --> fib(1) + fib(2) --> 1
# 
def f(n):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return f(n-2) + f(n-1)
    
# f(5) = 3