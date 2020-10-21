class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rec = rectangle      
        self.opList = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        # for i in range(row1, row2+1):
        #     for j in range(col1, col2+1):
        #         self.rec[i][j] = newValue
        self.opList.append((row1, row2, col1, col2, newValue))

    def getValue(self, row: int, col: int) -> int:
        
        for i in range(len(self.opList)-1, -1, -1):
            curr = self.opList[i]
            # print(curr, row, col)    
            if row>=curr[0] and row<=curr[1] and col>=curr[2] and col<=curr[3]:
                return curr[-1]
        return self.rec[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)