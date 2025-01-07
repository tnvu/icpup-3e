# Finger exercise: Replace the comment in the following code with a
# while loop.
#     num_x = int(input('How many times should I print the letter
#     X? '))
#     to_print = ''
#     #concatenate X to to_print num_x times
#     print(to_print)

num_x = int(input('How many times should I print the letter X? '))
to_print = ''
i = 0
while (i < num_x):
    to_print = to_print + 'X'
    i = i + 1
print(to_print)