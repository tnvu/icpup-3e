# Finger exercise: Use find to implement a function satisfying the
# specification
# def find_last(s, sub):
#   """s and sub are non-empty strings
#   Returns the index of the last occurrence of sub in s.
#   Returns None if sub does not occur in s"""

def find_last(s, sub):
    last = s.find(sub)
    if last == -1:
        # Not found
        return None
    while True:
        # Find next
        next = s.find(sub, last+1)
        if next == -1:
            break
        last = next
    return last