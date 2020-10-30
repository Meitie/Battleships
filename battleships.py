player_board = [[0 for i in range(11)] for j in range(11)]

for i in range(len(player_board)):
    player_board[i][0] = i

for i in range(1, 11):
    player_board[0][i] = chr(ord('A') + i - 1)

player_board[0][0] = ""

computer_board = player_board.copy()

dictionary_keys = []

for i in range(10):
    for j in range(1, 11):
        dictionary_keys.append(chr(ord('A') + i) + str(j))

dictoinary_vals = []

for i in range(1,11):
    for j in range(1,11):
        dictoinary_vals.append((i, j))

for i in dictionary_keys:
    print(i)

for i in dictoinary_vals:
    print(i)

print(len(dictionary_keys))

grid_system = {dictionary_keys[i]: dictoinary_vals[i] for i in range(len(dictionary_keys))}

# # grid_system = {dictionary_keys[i]: dictoinary_vals[i] for i in range(100)}


print(grid_system)


print("---------------------------------------------")
print("PLAYERS BOARD")
for i in player_board:
    print(i)

# print("---------------------------------------------")
# print("COMPUTERS BOARD")
# for i in computer_board:
#     print(i)
