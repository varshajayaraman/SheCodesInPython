class Solution:
    def findRow(self, matrix, tar, l, h):
        col = len(matrix[0]) - 1
        m = (l + h) // 2
        print("FindRow: ", m)
        if l > h:
            return -1
        if matrix[m][col] < tar:
            return self.findRow(matrix, tar, m + 1, h)
        else:
            if matrix[m][0] > tar:
                return self.findRow(matrix, tar, l, m - 1)
            else:
                return m

    def findEle(self, arr, tar, l, h):
        col = len(arr) - 1
        m = (l + h) // 2
        if l > h:
            return False

        if arr[m] == tar:
            return True
        elif arr[m] > tar:
            return self.findEle(arr, tar, l, m - 1)
        else:
            return self.findEle(arr, tar, m + 1, h)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        if rows == 0:
            return False
        cols = len(matrix[0])
        if cols == 0:
            return False

        r = self.findRow(matrix, target, 0, rows - 1)

        if r == -1:
            return False
        return self.findEle(matrix[r], target, 0, cols - 1)