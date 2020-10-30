import random

computer_board = [[0 for i in range(11)] for j in range(11)]

for i in range(len(computer_board)):
    computer_board[i][0] = i

for i in range(1, 11):
    computer_board[0][i] = chr(ord('A') + i - 1)

computer_board[0][0] = ""

print("---------------------------------------------")
print("COMPUTERS BOARD")
for i in computer_board:
    print(i)





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

    direction = random_direction()
    print(random_direction())
    if direction == 1:
        pass
    if direction == 2:
        pass
    if direction == 3:
        pass
    if direction == 4:
        pass

    print(f"The computer has set down its boats, Your Turn! :)")

computer_boats()