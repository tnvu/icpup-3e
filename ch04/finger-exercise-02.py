# Finger exercise: Write a function is_in that accepts two strings as
# arguments and returns True if either string occurs anywhere in the
# other, and False otherwise. Hint: you might want to use the built-in
# str operator in.

def is_in(s1, s2):
    return s1 in s2 or s2 in s1

def test_is_in(s1_vals, s2_vals):
    for s1 in s1_vals:
        for s2 in s2_vals:
            result = is_in(s1, s2)
            print(f'{s1}, {s2}: {result}')
s1_vals = ('abc', 'def')
s2_vals = ('a', 'b', 'c', 'ab', 'bc', 'ac',
           'abcdef', 'hijklmnop',
           'ed', 'fe', 'fd')
test_is_in(s1_vals, s2_vals)
