class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows_list = [set([]) for i in range(len(board))]
        cols_list = [set([]) for i in range(len(board[0]))]

        i = 0

        while i < len(board):
            j = 0
            while j < len(board[0]):
                sq_set = set([])
                for k in range(3):
                    for l in range(3):
                        if board[i + k][j + l] != ".":
                            num = board[i + k][j + l]
                            if num in sq_set or num in rows_list[i + k] or num in cols_list[j + l]:
                                return False
                            else:
                                sq_set.add(num)
                                rows_list[i + k].add(num)
                                cols_list[j + l].add(num)
                j += 3
            i += 3

        return True