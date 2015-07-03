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
    """ To get a random row from the board for players to guess """
    return randint(0, len(board) - 1)

def randomCol(board):
    """ To get a random column from the board for players to guess """
    return randint(0, len(board[0]) - 1)

def guessYourChoice(board, ship_row, ship_col):
        """ Get the choice from player and check whether the guess is correct and print the corresponding output"""
        printBoard(board)
        guess_row = int(input("Guess Row:"))
        guess_col = int(input("Guess Col:"))
        if guess_row == ship_row and guess_col == ship_col:   # if a player makes the right guess
           print ("Congratulations! You sunk my battleship!")
           sys.exit()
        else:
           if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4): # if a player guess is out of the defined matrix
              print ("Oops, that's not even in the ocean.")  
           elif(board[guess_row][guess_col] == "X"):   # when a player makes the same guess which he already did
              print ("You guessed that one already.")  
           else:
              print ("You missed my battleship!")  # when the guess is wrong
              board[guess_row][guess_col] = "X"

def letsPlayBattleship(board):
    ship_row = randomRow(board)
    ship_col = randomCol(board)
    print(ship_row, ship_col)
    print("Lets Play Battleship")
    for turn in range(3):   # to provide the player with three turns to make a right guess
        print(turn+1)
        guessYourChoice(board, ship_row, ship_col)

def main():
    board = createBoard()
    letsPlayBattleship(board)
    print("Game Over")

main()
