player_board = [[0 for i in range(11)] for j in range(11)]

for i in range(len(player_board)):
    player_board[i][0] = i

for i in range(1, 11):
    player_board[0][i] = chr(ord('A') + i - 1)

player_board[0][0] = ""

print("---------------------------------------------")
print("PLAYERS BOARD")
for i in player_board:
    print(i)

def player_boats():
    print(f"\nPlease get ready to place your 5 boats:")
    print(f"\nThe boats are follwoing in length:")
    print(f"Carrier (5), Battleship (4), Cruiser (3), Submarine (3), Destroyer(2)")
    player_boats = []
    carrier = input("Carrier: 5 in length, please enter the start: ")
    end = input("Please enter the end: ")
    player_boats.append((carrier, end))

    battleship = input("Battleship: 4 in length, please enter the start: ")
    end = input("Please enter the end: ")
    player_boats.append((battleship, end))

    cruiser = input("Cruiser: 3 in length, please enter the start: ")
    end = input("Please enter the end: ")
    player_boats.append((cruiser, end))

    submarine = input("Submarine: 3 in length, please enter the start: ")
    end = input("Please enter the end: ")
    player_boats.append((submarine, end))

    destroyer = input("Destroyer: 2 in length, please enter the start: ")
    end = input("Please enter the end: ")
    player_boats.append((destroyer, end))

    return player_boats

print(player_boats())