# Finger exercise: Write a program that asks the user to input 10
# integers, and then prints the largest odd number that was entered. If
# no odd number was entered, it should print a message to that effect.

num_integers = 10
i = 0
answer = 0
while (i < num_integers):
    n = int(input(f'Please enter an integer: '))
    if n % 2 != 0 and n > answer:
        answer = n
    i = i + 1
if answer == 0:
    print('No odd integers were entered.')
else:
    print(answer)
