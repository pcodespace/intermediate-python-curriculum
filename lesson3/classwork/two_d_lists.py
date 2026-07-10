# A 2D list can represent a grid
board = [
    [".", ".", "."],
    [".", "X", "."],
    [".", ".", "."]
]

# Print the board row by row
for row in range(len(board)):
    print(board[row])

# Change one spot in the board
board[0][2] = "O" # oard[row][column]
print("After change:")
for row in range(len(board)):
    print(board[row])