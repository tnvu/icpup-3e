# Finger exercise: What does the following code print?
# L = [1, 2, 3]
# L.append(L)
# print(L is L[-1])

# L = [1, 2, 3]         L ---> [1, 2, 3]
# L.append(L)           L ---> [1, 2, 3, .]
#                       ^                |
#                       |----------------|
# print(L is L[-1])     True
