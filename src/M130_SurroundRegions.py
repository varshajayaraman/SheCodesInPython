def markAdjacent(board, i, j):
    row = len(board)
    col = len(board[0])

    flag=False

    if i>0:
        if board[i-1][j]=='D':
            board[i][j]='D'
    if i < row-1:
        if board[i + 1][j] == 'D':
            board[i][j] = 'D'
    if j > 0:
        if board[i][j-1] == 'D':
            board[i][j] = 'D'
    if i <col-1:
        if board[i][j+1] == 'D':
            board[i][j] = 'D'

    return board


def solve(board):
    """
    Do not return anything, modify board in-place instead.
    """
    row = len(board)-1  # final row
    col = len(board[0])-1  # final col

    irow = 0  # initial row
    icol = 0  # initial col

    while irow <= row and icol <= col:
        print(row, col)
        for j in range(icol, col):
            if board[irow][j] == '0':
                if irow==0:
                    board[irow][j]='D'
                else:
                    board  = markAdjacent(board, irow, j)

        irow += 1

        for j in range(icol,col):
            if board[row][j] == '0':
                if board[row][j] == '0':
                    if row == len(board)-1:
                        board[row][j] = 'D'
                    else:
                        board = markAdjacent(board, row, j)
        row -= 1

        for i in range(irow, row):
            if board[i][icol] == '0':
                if board[i][icol] == '0':
                    if icol == 0:
                        board[i][icol] = 'D'
                    else:
                        board = markAdjacent(board, i, icol)
        icol += 1

        for i in range(irow, row):
            if board[i][col] == '0':
                if board[i][col] == '0':
                    if col == len(board[0])-1:
                        board[i][col] = 'D'
                    else:
                        board = markAdjacent(board, i, col)
        col -= 1

    print(board)