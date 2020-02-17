class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        row = len(matrix)
        if row == 0:
            return False
        col = len(matrix[0])
        i = row - 1
        j = 0

        while i >= 0 and i < row and j >= 0 and j < col:
            if matrix[i][j] < target:
                j += 1
            elif matrix[i][j] == target:
                return True
            else:
                i -= 1
        return False

