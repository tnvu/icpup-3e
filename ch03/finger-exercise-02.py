# Finger exercise: Write a program that asks the user to enter an
# integer and prints two integers, root and pwr, such that 1 < pwr < 6
# and root**pwr is equal to the integer entered by the user. If no such
# pair of integers exists, it should print a message to that effect.

x = int(input('Please enter an integer: '))
ans_root = None
ans_pow = None
for root in range(2, x):
    for pow in range(2, 6):
        if root**pow == x:
            ans_root = root
            ans_pow = pow
            break
    if ans_root != None:
        break

if ans_root == None:
    print('No pair of integers')
else:
    print(f'{x} == {ans_root}**{ans_pow}')
