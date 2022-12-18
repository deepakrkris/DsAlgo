def valid_position(board, row, current_col) :
    current_row = row
    row -= 1

    while row > 0 :
        if board[row] == current_col or board[row] == current_col - (current_row - row) or board[row] == current_col + (current_row - row) :
          return False
        row -= 1
    return True

def place_queen(N, row, board, result) :
    if row == N :
      result.append(''.join(board))

    for i in range(N) :
        if valid_position(board, row, i) :
            board.append(i)
            place_queen(N, row + 1, board, result)
            board.pop()

def solve_n_queens(n):
    result = []
    place_queen(n, 0, [], result)
    return len(result)
