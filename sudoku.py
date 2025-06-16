sudoku = [[0, 3, 4, 0],
          [4, 0, 0, 2],
          [1, 0, 0, 3],
          [0, 2, 1, 0]]
def is_valid(board, row, col, num):
    for i in range(4):
        if board[row][i] == num or board[col][i] == num:
            return False
        start_row = (row // 2) *2
        start_col = (col // 2) *2
        for i in range(start_row, start_row + 2):
            for j in range(start_col, start_col+2):
                if board[i][j] == num:
                    return False
        return True
def solve_sudoku(board):
    for row in range(0,4):
        for col in range(0,4):
            if board [row][col] == 0:
                for num in range(1,5):
                    if is_valid(board,row,col,num) == True:
                        board[row][col] = num
                        if solve_sudoku(board) == True:
                            return True
                        else:
                            board[row][col] = 0
                return False
    return True
def print_board(board):
    for row in board:
        print(" ".join(str(num) for num in row))
                        