class Solution:
    def isHappy(self, n: int) -> bool:

        refDict = {}
        sumVal = 0
        num = n
        while sumVal not in refDict:
            refDict[sumVal] = 1
            digits = list(str(num))
            print(digits)
            digits = [int(i) * int(i) for i in digits]
            sumVal = sum(digits)
            if sumVal == 1:
                return True
            # if sumVal == 0:
            #     return False
            num = sumVal
            print(sumVal)
        return False