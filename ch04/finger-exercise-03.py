# Finger exercise: Write a function to test is_in.

def test_is_in(s1_vals, s2_vals):
    for s1 in s1_vals:
        for s2 in s2_vals:
            result = is_in(s1, s2)
            print(f'{s1}, {s2}: {result}')