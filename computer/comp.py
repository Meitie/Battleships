import random

computer_board = [[0 for i in range(11)] for j in range(11)]

for i in range(len(computer_board)):
    computer_board[0][i] = i

for i in range(1, 11):
    computer_board[i][0] = chr(ord('A') + i - 1)

computer_board[0][0] = ""

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
        print(f"aa: {letter_cord} bb {chr(ord(letter_cord) + ship_size)}")
        if chr(ord(letter_cord) + ship_size) <= chr(ord('J')):
            return True
        else:
            return False


def end_boat(boat_cords, direction, ship_size):
    letter_cord = boat_cords[0]
    num_cord = boat_cords[1]
    letter_cord = chr(ord(letter_cord) + ship_size)
    boat_cords = letter_cord+num_cord
    print("boat_cords", boat_cords)
    return boat_cords

def random_direction():
    return random.randint(1,4)


def computer_boats():
    carrier = f"{chr(random.randint(ord('A'), ord('J')))}{random.randint(1,10)}"
    battleship = f"{chr(random.randint(ord('A'), ord('J')))}{random.randint(1,10)}"
    cruiser = f"{chr(random.randint(ord('A'), ord('J')))}{random.randint(1,10)}"
    submarine = f"{chr(random.randint(ord('A'), ord('J')))}{random.randint(1,10)}"
    destroyer = f"{chr(random.randint(ord('A'), ord('J')))}{random.randint(1,10)}"

    print(f"carrier: {carrier}\nbattleships: {battleship}\ncruiser: {cruiser}\nsubmarine: {submarine} \ndestroyer: {destroyer}")

    boats = [carrier, battleship, cruiser, submarine, destroyer]
    print(boats)

    # for i in range(len(boats)):
    #     letter.split(chr(),boats)

    # direction = random_direction()
    direction = 2
    print(random_direction())
    if direction == 1:
        print(battleship)
    if direction == 2:
        print(battleship)
        if inside_grid(battleship, direction, 5):
            battleship = (battleship, end_boat(battleship, direction, 4))
            print(battleship)
    if direction == 3:
        print(battleship)
    if direction == 4:
        print(battleship)

    print(f"The computer has set down its boats, Your Turn! :)")

computer_boats()
