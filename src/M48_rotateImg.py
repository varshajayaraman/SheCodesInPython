class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n == 1:
            return matrix

        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                # print(i,j)
                t = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][i]
                matrix[n - j - 1][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = t
