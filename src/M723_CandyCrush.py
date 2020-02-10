class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:

        def p(board):
            for f in board:
                print(f)

        def reassemble(board):
            # p(board)
            row = len(board)
            col = len(board[0])
            wr = row - 1

            for j in range(col - 1, -1, -1):
                wr = row - 1
                for i in range(row - 1, -1, -1):

                    if board[i][j] > 0:
                        t = board[wr][j]
                        board[wr][j] = board[i][j]
                        board[i][j] = t
                        wr -= 1
                # print(board)
                # if wr<row-1:
                while wr >= 0:
                    if board[wr][j] < 0:
                        board[wr][j] = 0
                    else:
                        break
                    wr -= 1

            p(board)
            return board

        row = len(board)
        col = len(board[0])
        changed = False
        while 1:
            print(changed)
            changed = False
            for i in range(row):
                for j in range(col - 2):
                    if abs(board[i][j]) == abs(board[i][j + 1]) == abs(board[i][j + 2]) and abs(board[i][j]) != 0:
                        changed = True
                        board[i][j] = board[i][j + 1] = board[i][j + 2] = -abs(board[i][j])

            for i in range(row - 2):
                for j in range(col):
                    if abs(board[i][j]) == abs(board[i + 1][j]) == abs(board[i + 2][j]) and abs(board[i][j]) != 0:
                        changed = True
                        board[i][j] = board[i + 1][j] = board[i + 2][j] = -abs(board[i][j])

            if changed:
                board = reassemble(board)
            else:
                return board