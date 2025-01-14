# Finger exercise: Implement a function that meets the specification
# def get_min(d):
#   """d a dict mapping letters to ints
#   returns the value in d with the key that occurs first
#   in the alphabet. E.g., if d = {x = 11, b = 12}, get_min
#   returns 12."""

def get_min(d):
    """d is a dict mapping letters to ints
    returns the value in d with the key that occurs first
    in the alphabet. E.g., if d = {x = 11, b = 12}, get_min returns 12"""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    min_index = None
    min_val = None
    for k, v in d.items():
        index = alphabet.find(k.lower())
        if index != -1 and (min_index == None or index < min_index):
            min_index = index
            min_val = v
    return min_val
