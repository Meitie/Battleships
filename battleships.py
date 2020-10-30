dictionary_keys = []

for i in range(10):
    for j in range(1, 11):
        dictionary_keys.append(chr(ord('A') + i) + str(j))

dictoinary_vals = []

for i in range(1,11):
    for j in range(1,11):
        dictoinary_vals.append((i, j))

grid_system = {dictionary_keys[i]: dictoinary_vals[i] for i in range(len(dictionary_keys))}

print(grid_system)