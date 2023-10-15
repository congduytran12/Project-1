#PYTHON 
def is_valid(board, row, col, num):
    if num in board[row]:
        return False
    if num in [board[i][col] for i in range(9)]:
        return False   
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return 1    
    row, col = empty_cell
    count = 0   
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            count += solve_sudoku(board)
            board[row][col] = 0     
    return count

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

board = []
for i in range(9):
    row = list(map(int, input().split()))
    board.append(row)

print(solve_sudoku(board))
