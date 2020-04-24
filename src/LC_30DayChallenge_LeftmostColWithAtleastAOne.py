class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        global last
        last = -1

        row, col = binaryMatrix.dimensions()
        bm = binaryMatrix

        r = 0
        c = col - 1
        while r < row and c >= 0:
            if bm.get(r, c) == 1:
                last = c
                c -= 1
            else:
                r += 1

        return last