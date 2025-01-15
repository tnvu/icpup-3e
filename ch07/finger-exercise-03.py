# Finger exercise: Write a program that first stores the first ten
# numbers in the Fibonnaci sequence to a file named fib_file. Each
# number should be on a separate line in the file. The program should
# then read the numbers from the file and print them.

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)
    
with open('fib_file', 'w') as fib_file:
    for i in range(0, 10):
        fib_file.write(str(fib(i)) + '\n')

with open('fib_file', 'r') as fib_file:
    for l in fib_file:
        print(l[:-1])

# remove fib_file
import os
os.unlink('fib_file')