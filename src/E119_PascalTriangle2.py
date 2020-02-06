class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        temp = [1, 1]
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return temp

        for i in range(2, rowIndex + 1):
            new = []
            for j in range(i + 1):
                if j == 0:
                    new.append(temp[0])
                elif j == i:
                    new.append(temp[j - 1])
                else:
                    new.append(temp[j - 1] + temp[j])
            temp = new
        return temp
