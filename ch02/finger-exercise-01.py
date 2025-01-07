# Finger exercise: Write a program that examines three variables—
# x, y, and z—and prints the largest odd number among them. If none
# of them are odd, it should print the smallest value of the three.


x = 1
y = 3
z = 5

answer = min(x, y, z)
if x % 2 != 0:
    answer = x
if y % 2 != 0 and y > answer:
    answer = y
if z % 2 != 0 and z > answer:
    answer = z
print(answer)