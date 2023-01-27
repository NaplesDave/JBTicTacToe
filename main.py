# TicTacToe game for JetBrains Academy Project
# stage 5 of 5 - Passing Code
# David A. King
# Jan 27, 2023
# code they don't use is commented out for this phase of the project
# it could be cleaner, but it works.
# X goes first, enter coordinates in pairs IE: 1 1  or 3 2

player = "X"
cells = list("_" * 9)  # establish blank play board


def change_player():
    global player
    if player == "O":
        player = "X"
    else:
        player = "O"


def print_grid():
    global cells
    print("---------")
    print(f"| {cells[0]} {cells[1]} {cells[2]} |")
    print(f"| {cells[3]} {cells[4]} {cells[5]} |")
    print(f"| {cells[6]} {cells[7]} {cells[8]} |")
    print("---------")


def check_status(plr):
    # check to see if winner in rows across
    if plr == cells[0] and plr == cells[1] and plr == cells[2]:
        return "wins"
    elif plr == cells[3] and plr == cells[4] and plr == cells[5]:
        return "wins"
    elif plr == cells[6] and plr == cells[7] and plr == cells[8]:
        return "wins"
    # check to see if winner in cols down
    elif plr == cells[0] and plr == cells[3] and plr == cells[6]:
        return "wins"
    elif plr == cells[1] and plr == cells[4] and plr == cells[7]:
        return "wins"
    elif plr == cells[2] and plr == cells[5] and plr == cells[8]:
        return "wins"
    # check diagonal wins
    elif plr == cells[2] and plr == cells[4] and plr == cells[6]:
        return "wins"
    elif plr == cells[0] and plr == cells[4] and plr == cells[8]:
        return "wins"
    # check to see if cells are not filled so game is in play
    # elif '_' in cells:
    # return 'Game Not Over'
    # check to see if all cells are filled so and nobody won above, so it is a Draw
    elif '_' not in cells:
        return "Draw"
    else:
        return ' '


# def check_impossible():
#     if ansO == 'O wins' and ansX == 'X wins':
#         return True
#     count_x = cells.count('X')
#     count_o = cells.count('O')
#     diff = abs(count_x - count_o)
#     if diff > 1:
#         return True


def check_num_in(x, y):
    # check for valid range of numbers
    valid_values = "123"
    if x not in valid_values or y not in valid_values:
        return True


def check_is_alpha(x, y):
    if not x.isdigit() or not y.isdigit():
        return True


playing = True
while playing:

    print_grid()  # show the playing board
    # ansO = check_status('O')
    # ansX = check_status('X')
    # if check_impossible():
    # print("Impossible")
    # if ansO[0] == 'O' and ansX != 'X':
    #     print(ansO)
    # elif ansX[0] == 'X' and ansO != 'O':
    #     print(ansX)
    # elif ansO[0] == 'G' and ansX[0] == 'G':
    # print("Game not finished")
    # if ansO[0] == 'D' and ansX[0] == 'D':
    #     print("Draw")
    # elif check_impossible():
    #     print("Impossible")
    getcoords = True
    while getcoords:
        coords = input()
        check_for_alpha = check_is_alpha(coords[0], coords[2])
        if check_for_alpha:
            print("You should enter numbers!")
            continue
        elif check_num_in(coords[0], coords[2]):
            # input not in 1-3 range
            print("Coordinates should be from 1 to 3!")
            continue

        movein = ((int(coords[0]) - 1) * 3) + ((int(coords[2]) + 2) - 3)

        if cells[movein] != '_':
            print("This cell is occupied! Choose another one!")
            continue
        else:
            cells[movein] = player
            ansO = check_status('O')
            ansX = check_status('X')
            print_grid()
            change_player()

        if ansO[0] == 'D' and ansX[0] == 'D':
            print("Draw")
            getcoords = False
            playing = False
        elif ansO[0] == 'w' :
            print("O wins")
            getcoords = False
            playing = False
        elif ansX[0] == 'w':
            print("X wins")
            getcoords = False
            playing = False


