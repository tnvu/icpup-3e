# Finger exercise: The Empire State Building is 102 stories high. A
# man wanted to know the highest floor from which he could drop an
# egg without the egg breaking. He proposed to drop an egg from the
# top floor. If it broke, he would go down a floor, and try it again. He
# would do this until the egg did not break. At worst, this method
# requires 102 eggs. Implement a method that at worst uses seven
# eggs.

true_answer = 1

high = 102
low = 1
ans = (high + low) // 2
num_guesses = 0
while (high - low) > 1:
    print(f'low={low}, high={high}, ans={ans}')
    if ans > true_answer:
        # egg broke
        high = ans
    else:
        low = ans
    ans = (high + low) // 2
    num_guesses += 1
print(f'ans={ans}, num_guesses={num_guesses}')