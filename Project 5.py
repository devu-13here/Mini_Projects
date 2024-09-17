# Tic-Tac-Toe Program with manual input in Python

# importing all necessary libraries
import numpy as np
from time import sleep

# Creates an empty board
def create_board():
    return np.array([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])

# Check for empty places on board
def possibilities(board):
    l = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                l.append((i, j))
    return l

# Manual input for player
def manual_place(board, player):
    print(f"Player {player}'s turn.")
    while True:
        try:
            row = int(input("Enter the row (1, 2, 3): ")) - 1
            col = int(input("Enter the column (1, 2, 3): ")) - 1
            if (row, col) in possibilities(board):
                board[row, col] = player
                break
            else:
                print("The position is already taken or invalid. Try again.")
        except ValueError:
            print("Invalid input! Please enter a valid row and column.")
    return board

# Checks whether the player has three in a horizontal row
def row_win(board, player):
    for x in range(len(board)):
        if np.all(board[x, :] == player):
            return True
    return False

# Checks whether the player has three in a vertical row
def col_win(board, player):
    for x in range(len(board)):
        if np.all(board[:, x] == player):
            return True
    return False

# Checks whether the player has three in a diagonal row
def diag_win(board, player):
    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True
    return False

# Evaluates whether there is a winner or a tie
def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1  # Tie
    return winner

# Main function to start the game
def play_game():
    board, winner, counter = create_board(), 0, 1
    print(board)
    
    while winner == 0:
        for player in [1, 2]:
            board = manual_place(board, player)
            print(f"Board after {counter} move:")
            print(board)
            counter += 1
            winner = evaluate(board)
            if winner != 0:
                break
    
    return winner

# Driver Code
result = play_game()

if result == -1:
    print("It's a tie!")
else:
    print(f"Winner is: Player {result}")
