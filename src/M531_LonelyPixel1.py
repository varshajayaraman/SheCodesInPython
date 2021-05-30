class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        rows = len(picture)
        cols = len(picture[0])
        maxCount = 0
        for i in range(rows):
            rowCount = 0
            col = -1
            for j in range(cols):
                if picture[i][j] == "B":
                    if rowCount == 0:
                        col = j
                        rowCount = 1
                    else:
                        rowCount = 2
                        break
            if rowCount == 1:
                colCount = 0
                for i in range(rows):
                        if picture[i][col] == "B":
                            if colCount == 0:
                                colCount = 1
                            else:
                                colCount = 2
                                break
                if colCount==1:
                    maxCount +=1
        return maxCount