from random import randint
import sys
def createBoard():
    """ create a broard of matrix 5 by 5"""
    board = []
    for x in range(5):
        board.append(["O"] * 5)    
    return board

def printBoard(board):
    """ To print the created board"""
    for row in board:
        print (" ".join(row))
    
def randomRow(board):
    return randint(0, len(board) - 1)

def randomCol(board):
    return randint(0, len(board[0]) - 1)

def guessYourChoice(board, ship_row, ship_col):
        printBoard(board)
        guess_row = int(input("Guess Row:"))
        guess_col = int(input("Guess Col:"))
        if guess_row == ship_row and guess_col == ship_col:
           print ("Congratulations! You sunk my battleship!")
           sys.exit()
        else:
           if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
              print ("Oops, that's not even in the ocean.")
           elif(board[guess_row][guess_col] == "X"):
              print ("You guessed that one already.")
           else:
              print ("You missed my battleship!")
              board[guess_row][guess_col] = "X"

def letsPlayBattleship(board):
    ship_row = randomRow(board)
    ship_col = randomCol(board)
    print(ship_row, ship_col)
    print("Lets Play Battleship")
    for turn in range(3):
        print(turn+1)
        guessYourChoice(board, ship_row, ship_col)

def main():
    board = createBoard()
    letsPlayBattleship(board)
    print("Game Over")

main()
