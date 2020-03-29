class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.dim = n
        self.board = [[0 for i in range(n)] for j in range(n)]

    def checkHorizontal(self, r, c):
        val = self.board[r][c]
        for j in range(self.dim):
            if self.board[r][j] != val:
                return False
        return True

    def checkVertical(self, r, c):
        val = self.board[r][c]
        for i in range(self.dim):
            if self.board[i][c] != val:
                return False
        return True

    def checkDiagonal(self, r, c):
        win = True
        val = self.board[r][c]
        for m in range(self.dim):
            if self.board[m][m] != val:
                win = False
                break
        if win is False:
            for m in range(self.dim):
                if self.board[m][self.dim - 1 - m] != val:
                    return False
        return True

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """

        self.board[row][col] = player
        if self.checkHorizontal(row, col) or self.checkVertical(row, col) or self.checkDiagonal(row, col):
            return player % 3
        return 0
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)