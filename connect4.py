gameMap = [[" ", " ", " ", " ", " ", " ", " ", " ", " "],
           ["|", " ", " ", " ", " ", " ", " ", " ", "|"],
           ["|", " ", " ", " ", " ", " ", " ", " ", "|"],
           ["|", " ", " ", " ", " ", " ", " ", " ", "|"],
           ["|", " ", " ", " ", " ", " ", " ", " ", "|"],
           ["|", " ", " ", " ", " ", " ", " ", " ", "|"],
           ["|", " ", " ", " ", " ", " ", " ", " ", "|"],
           ["#", "-", "-", "-", "-", "-", "-", "-", "#"]]


def display_map():
    print("| 1 2 3 4 5 6 7 |")
    for i in gameMap:
        for j in i:
            print(j, end=" ")
        print()


def place_token(token):
    move = int(input(token + " Choose a column to place your token: "))
    while move <= 0 or move >= 8:
        print("INVALID column try again: ")
        move = int(input(token + " Choose a column to place your token: "))
    else:
        i = 6
        while gameMap[i][move] == '$' or gameMap[i][move] == '@':
            i = i - 1

        if i == 0:
            print("INVALID column try again: ")
        elif gameMap[i][move] == " ":
            gameMap[i][move] = token
            display_map()


def check_win(token):
    for x in range(len(gameMap)):
        for y in range(len(gameMap)):
            if gameMap[x][y] == token and gameMap[x][y + 1] == token and gameMap[x][y + 2] == token and \
                    gameMap[x][y + 3] == token:  # vertical win
                print("Winner " + token)
                print("Game over")
                quit()

            if gameMap[x][y] == token and gameMap[x + 1][y] == token and gameMap[x + 2][y] == token and \
                    gameMap[x + 3][y] == token:  # horizontal win
                print("Winner " + token)
                print("Game over")
                quit()

            if gameMap[x][y] == token and gameMap[x + 1][y + 1] == token and gameMap[x + 2][y + 2] == token and \
                    gameMap[x + 3][y + 3] == token:  # diagonal win
                print("Winner " + token)
                print("Game over")
                quit()

            if gameMap[x][y] == token and gameMap[x + 1][y - 1] == token and gameMap[x + 2][y - 2] == token and \
                    gameMap[x + 3][y - 3] == token:  # diagonal win
                print("Winner " + token)
                print("Game over")
                quit()


def main():
    display_map()
    while True:

        player1 = '$'
        player2 = '@'

        place_token(player1)
        check_win(player1)
        place_token(player2)
        check_win(player2)


main()