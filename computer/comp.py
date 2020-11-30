import random

def set_up_board():
    computer_board = [['0' for i in range(11)] for j in range(11)]

    for i in range(len(computer_board)):
        computer_board[0][i] = str(i)

    for i in range(1, 11):
        computer_board[i][0] = chr(ord('A') + i - 1)

    computer_board[0][0] = ""
    return computer_board


def dictionary_board():
    dictionary_keys = []

    for i in range(10):
        for j in range(1, 11):
            dictionary_keys.append(chr(ord('A') + i) + str(j))

    dictoinary_vals = []

    for i in range(1,11):
        for j in range(1,11):
            dictoinary_vals.append((i, j))

    grid_system = {dictionary_keys[i]: dictoinary_vals[i] for i in range(len(dictionary_keys))}

    # print(grid_system)
    return grid_system



def print_board(computer_board):
    print("---------------------------------------------")
    print("COMPUTERS BOARD")
    for i in computer_board:
        print(i)


def inside_grid(boat_cords, direction, ship_size):
    """SWAP AROUND"""
    letter_cord = boat_cords[0]
    num_cord = boat_cords[1]
    if direction == 1 or direction == 3:
        if int(num_cord) + ship_size <= 10:
            return True
        else:
            return False
    elif direction == 2 or direction == 4:
        if chr(ord(letter_cord) + ship_size) <= chr(ord('J')):
            return True
        else:
            return False


def end_boat(boat_cords, direction, ship_size):
    letter_cord = boat_cords[0]
    num_cord = boat_cords[1]
    letter_cord = chr(ord(letter_cord) + ship_size - 1)
    boat_cords = letter_cord+num_cord
    print("boat_cords", boat_cords)
    return boat_cords

def random_direction():
    return random.randint(1,4)


def setup_boats():
    ships = {
        "carrier": f"{chr(random.randint(ord('A'), ord('J')))}{random.randint(1,10)}",
        "battleship": f"{chr(random.randint(ord('A'), ord('J')))}{random.randint(1,10)}",
        "cruiser": f"{chr(random.randint(ord('A'), ord('J')))}{random.randint(1,10)}",
        "submarine": f"{chr(random.randint(ord('A'), ord('J')))}{random.randint(1,10)}",
        "destroyer": f"{chr(random.randint(ord('A'), ord('J')))}{random.randint(1,10)}",
    }
    return ships


def print_to_board(board, dict_board, boat_cords):
    print(boat_cords)
    if boat_cords[0][1] == boat_cords[1][1]:
        x = ord(boat_cords[0][0]) - ord("A") + 1
        y = ord(boat_cords[1][0]) - ord("A") + 1
        for i in range(x, y + 1):
            board[i][dict_board[boat_cords[0]][1]] = 's'
        print_board(board)
    else:
        print("letter")


def place_boats(ships, board, dict_board):
    direction = 2
    # direction = random_direction()
    # print(direction)
    if direction == 1:
        pass
        # place_boats(ships, board, dict_board)
    elif direction == 2:
        print(ships["battleship"])
        if inside_grid(ships["battleship"], direction, 4):
            battleship = (ships["battleship"], end_boat(ships["battleship"], direction, 4))
            print_to_board(board, dict_board, battleship)
        else:
            print("reset_it")
            # place_boats(ships, board, dict_board)
    elif direction == 3:
        pass
        # place_boats(ships, board, dict_board)
    elif direction == 4:
        pass
        # place_boats(ships, board, dict_board)
    


def computer_boats():
    board = set_up_board()
    # print_board(board)
    ships = setup_boats()
    dict_board = dictionary_board()

    place_boats(ships, board, dict_board)

    print(f"The computer has set down its boats, Your Turn! :)")

computer_boats()
