# Create a list of three lists of three items each. Inspect the structure.
board = [['_'] * 3 for i in range(3)]
print(board)

board[1][2] = 'X'
print(board)