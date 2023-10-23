global N
N = 4

# Function to check
def isSafe(board, row, col):
    # Check in row (left-side)
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check in upper-left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check in down-left diagonal
    for i, j in zip(range(row+1, N, 1), range(col-1 , -1, -1)):
        if board[i][j] == 1:
            return False
    return True
    
def n_queens(board, col):
    # base condition
    if col == len(board):
        return True
    
    for row in range(N):
        if isSafe(board, row, col):
            board[row][col] = 1
            if n_queens(board, col + 1) == True:
                return True
            board[row][col] = 0
    return False

# Driver Code
board = [[0 for j in range(N)] for i in range(N)]
if n_queens(board, 0) == True:
    for i in range(N):
        for j in range(N):
            print(board[i][j], end = " ")
        print()

