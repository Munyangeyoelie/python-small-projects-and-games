#create board  and curent player who will be equal to x 
board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-", ]

curentPlayer = "X"
winner = None
gamerunning = True

# Print the game board that you just created 
def printBoard(board): 
    print(board[0] + "|" + board [2] + "|" + board [3])
    print(board[4] + "|" + board [5] + "|" + board [6])
    print(board[7] + "|" + board [8] + "|" + board [9])
    printBoard(board)