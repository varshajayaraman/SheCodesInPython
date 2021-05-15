class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        cnt = 0

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    if i == 0:
                        if j == 0:
                            cnt += 1
                        elif board[i][j - 1] != 'X':
                            cnt += 1
                    elif j == 0:
                        if board[i - 1][j] != 'X':
                            cnt += 1
                    else:
                        if board[i - 1][j] != 'X' and board[i][j - 1] != 'X':
                            cnt += 1
        return cnt