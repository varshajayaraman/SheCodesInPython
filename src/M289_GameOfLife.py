class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # -1 - Dead
        # -2 - Alive

        neighbours = [(1, 0), (-1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
        if len(board) == 0:
            return board
        row = len(board)
        col = len(board[0])
        for i in range(len(board)):
            for j in range(len(board[0])):
                r = i
                c = j
                sumVal = 0
                for n in neighbours:
                    r = i + n[0]
                    c = j + n[1]

                    if r < 0 or r == row or c < 0 or c == col:
                        continue
                    else:
                        if board[i][j] == 0:
                            if board[r][c] == 1 or board[r][c] == -1:
                                sumVal += 1
                                # print(i,j, r,c,sumVal)
                        else:
                            if board[r][c] == 1 or board[r][c] == -1:
                                # or board[r][c]==-2:
                                sumVal += 1
                                # print(i,j, r,c,sumVal)

                if board[i][j] == 0:
                    if sumVal == 3:
                        board[i][j] = -2
                    # else:

                elif board[i][j] == 1:
                    # if i==0and j==1:
                    # print(sumVal)
                    if sumVal < 2 or sumVal > 3:
                        # print("k")
                        board[i][j] = -1

        # print(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == -2 or board[i][j] == 1:
                    board[i][j] = 1
                else:
                    board[i][j] = 0

        return board
