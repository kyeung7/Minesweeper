# Python implementation of minesweeper

import random

# Part 5
# Randomly generate k bombs represented by "X" in the grid, neighboring
# cells increase value accordingly. Different levels represented as:
# Beginner (n=5, k=3), Intermediate (n=6, k=8), Expert (n=8, k=20)
def CreateBoard(tiles, bombs):
    arr = [[0 for row in range(tiles)] for column in range(tiles)]

    for num in range(bombs):
        x = random.randint(0, tiles - 1)
        y = random.randint(0, tiles - 1)
        arr[y][x] = "X"

        if (x >= 0 and x <= tiles - 2) and (y >= 0 and y <= tiles - 1):
            if arr[y][x + 1] != "X":
                arr[y][x + 1] += 1 # center right

        if (x >= 1 and x <= tiles - 1) and (y >= 0 and y <= tiles - 1):
            if arr[y - 1][x - 1] != "X":
                arr[y - 1][x - 1] += 1 # center left

        if (x >= 1 and x <= tiles - 1) and (y >= 1 and y <= tiles - 1):
            if arr[y - 1][x - 1] != "X":
                arr[y - 1][x - 1] += 1 #top left

        if (x >= 0 and x <= tiles - 2) and (y >= 1 and y <= tiles - 1):
            if arr[y - 1][x + 1] != "X":
                arr[y - 1][x + 1] += 1 #top right

        if (x >= 0 and x <= tiles - 1) and (y >= 1 and y <= tiles - 1):
            if arr[y - 1][x] != "X":
                arr[y - 1][x] += 1 #top center

        if (x >= 0 and x <= tiles - 2) and (y >= 0 and y <= tiles - 2):
            if arr[y + 1][x + 1] != "X":
                arr[y + 1][x + 1] += 1 #bottom right

        if (x >= 1 and x <= tiles - 1) and (y >= 0 and y <= tiles - 2):
            if arr[y + 1][x - 1] != "X":
                arr[y + 1][x - 1] += 1 #bottom left

        if (x >= 0 and x <= tiles - 1) and (y >= 0 and y <= tiles - 2):
            if arr[y + 1][x] != "X":
                arr[y + 1][x] += 1 #bottom center
    return arr

def BoardToString(tiles):
    arr = [["-" for row in range(tiles)] for column in range(tiles)]
    return arr
    
def DisplayBoard(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))
        print("")

def CheckWon(board):            
    for row in board:
        for cell in row:
            if cell =="-":
                return False
    return True

def CheckContinueGame(score):
    print("Your Score: ", score)
    isContinue = input("do you want to try again? (y/n) :")
    if isContinue == "n":
        return False
    return True

def Game():
    GameStatus = True
    while GameStatus:
        difficulty = input("select difficulty... Beginner(b), Intermediate(i), Expert(e):")

        if difficulty.lower() == "b":
            tiles = 5
            bombs = 3
        elif difficulty.lower() == "i":
            Tiles = 6
            bombs = 8
        elif difficulty.lower() == "e":
            tiles = 8
            bombs = 20
        
        minesweeper_board = CreateBoard(tiles, bombs)
        player_board = BoardToString(tiles)
        score = 0

        while True:
            if CheckWon(player_board) == False:
                print("enter cell u want to open:")
                x = int(input("X (1 to 5) :"))
                y = int(input("Y (1 to 5) :"))
                x = int(x) - 1 #0 based indexing
                x = int(y) - 1 #0 based indexing

                if(minesweeper_board[y][x] == "X"):
                    print("Game over")
                    DisplayBoard(minesweeper_board)
                    GameStatus = CheckContinueGame(score)
                    break
                else:
                    player_board[y][x] = minesweeper_board[y][x]
                    DisplayBoard(player_board)
                    score += 1
            else:
                DisplayBoard(player_board)
                print("You won")
                GameStatus = CheckContinueGame(score)
                break
                
if __name__ =="__main__":
    try:
        Game()
    except KeyboardInterrupt:
        print("ENDING GAME")
