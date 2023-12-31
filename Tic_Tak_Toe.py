def displayTheBoard(playingBox):
    print('\n\n\n')
    for row in range(3):
        for col in range(3):
            print('|', playingBox[row][col], '|', end='')
        print('\n---------------')
    print('\n\n\n')


def checkIfUser_X_or_Y_winner(playingBox, player):
    for i in range(3):
        if all(position == player for position in playingBox[i]) or \
           all(row[i] == player for row in playingBox) or \
           all(playingBox[i][i] == player for i in range(3)) or \
           all(playingBox[i][2 - i] == player for i in range(3)):
            return True
    return False


def checkIfDraw(playingBox):
    return all(position == 'X' or position == 'O' for row in playingBox for position in row)


def getPlayerInput(is_xTurn):
    while True:
        print('----------------------------------------------------------------')
        val = input('Player ' + (' < X > ' if is_xTurn else ' < O > ') + 'Choose a number: ')
        print('----------------------------------------------------------------')

        try:
            userInput = int(val)
            if (userInput < 1) or (userInput > 9):
                print("Invalid input please choose a number between 1 and 9.")
                continue
        except ValueError:
            print("Invalid input  Please enter a numbers only.")
            continue

        return userInput


def updatePlayingBox(playingBox, row, col, is_xTurn):
    if (playingBox[row][col] == 'X') or (playingBox[row][col] == 'O'):
        print("Cell already taken before. Choose another number.")
        return False

    if is_xTurn:
        playingBox[row][col] = 'X'
    else:
        playingBox[row][col] = 'O'

    return True


def main():
    playingBox = [
              ['1', '2', '3'],
              ['4', '5', '6'],
              ['7', '8', '9']
            ]
    displayTheBoard(playingBox)

    is_xTurn = True

    while True:
        userInput = getPlayerInput(is_xTurn)

        row = (userInput - 1) // 3
        col = (userInput - 1) % 3

        if not updatePlayingBox(playingBox, row, col, is_xTurn):
            continue

        displayTheBoard(playingBox)

        if checkIfUser_X_or_Y_winner(playingBox, 'X'):
            print("\n\nCongratulations Player X wins\n\n")
            break
        elif checkIfUser_X_or_Y_winner(playingBox, 'O'):
            print("\n\nCongratulations Player O wins\n\n")
            break
        elif checkIfDraw(playingBox):
            print("\n\nIt's a Tie\n\n")
            break

        is_xTurn = not is_xTurn

main()
while True:
    choice = input('\n\n\nPress "y" to continue OR "n" to exit \n\n\n')
    if choice.lower() == 'y':
        main()
    else:
        print('See you soon :)')
        break